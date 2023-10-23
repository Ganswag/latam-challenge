import apache_beam as beam
from apache_beam import CombinePerKey, Pipeline, FlatMap, Map, Regex
from apache_beam.io import ReadFromText, WriteToText
from apache_beam.options.pipeline_options import PipelineOptions

from src.modules.constants import TOP_N
from src.pipelines.helpers.q2_q3_helpers import parse_element


def run(file_path, pipeline_args=None):
    """Run a defined pipeline to compute the top 10 used emojis and their
    counter from a file and store the results in the relative path 
    './results/q3/' with the prefix 'results.txt'.
    
    Parameters:
    file_path (srt): a path where is located the file we want to read
    pipeline_args (dict): pipeline execution arguments, check 
    https://cloud.google.com/dataflow/docs/guides/setting-pipeline-options#python_2
    for more info
    """
    pipeline_options = PipelineOptions(
        pipeline_args, save_main_session=True,
    )

    with Pipeline(options=pipeline_options) as pipeline:
        (
            pipeline
            | 'Read file' >> ReadFromText(file_path)
            | 'Use the desired field' >> Map(parse_element)
            | 'Get mentions' >> Regex.find_all(r'(?<=@)(\w+)\b')
            | 'Flat elements' >> FlatMap(lambda x: x)
            | 'Map to (key, 1)' >> Map(lambda x: (x, 1))
            | 'And sum by key' >> CombinePerKey(sum)
            | "Select top N" >> beam.combiners.Top.Largest(
                TOP_N, key=lambda x: x[1]
            )
            | 'Persist results' >> WriteToText('./results/q3/results.txt')
        )
