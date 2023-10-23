import apache_beam as beam
from apache_beam import Pipeline, Map, GroupBy, CombineValues
from apache_beam.io import ReadFromText
from apache_beam.options.pipeline_options import PipelineOptions

from src.pipelines.custom_fn.max_fn import MaxFn
from src.pipelines.helpers.q1_helpers import parse_element, format_output
from src.modules.constants import TOP_N

DATE_INDEX = 0


def run(file_path, pipeline_args=None) -> None:
    """Run a defined pipeline to compute the most active user by the
    date with top 10 tweets from a file and store the results in the
    relative path './results/q1/' with the prefix 'results.txt'.
    
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
            | 'Group all users by date' >> GroupBy(lambda x: x[DATE_INDEX])
            | 'Get most active user per date' >> CombineValues(MaxFn())
            | 'Select Top 10' >> beam.combiners.Top.Largest(
                TOP_N, key=lambda x: x[1][0]
            )
            | 'Format to expected output' >> Map(format_output)
            | 'Persist results' >> beam.io.WriteToText(
                './results/q1/results.txt')
        )
