import apache_beam as beam
from apache_beam import CombinePerKey, Pipeline, FlatMap, Map
from apache_beam.io import ReadFromText, WriteToText
from apache_beam.options.pipeline_options import PipelineOptions
import emoji

from src.modules.constants import TOP_N
from src.pipelines.helpers.q2_q3_helpers import parse_element


def run(file_path, pipeline_args=None):
    pipeline_options = PipelineOptions(
        pipeline_args, save_main_session=True,
    )

    with Pipeline(options=pipeline_options) as pipeline:
        (
            pipeline
            | 'Read file' >> ReadFromText(file_path)
            | 'Use the desired field' >> Map(parse_element)
            | 'Get emojis' >> Map(
                lambda x: [el['emoji'] for el in emoji.emoji_list(x)]
            )
            | 'Flat elements' >> FlatMap(lambda x: x)
            | 'Map to key / value' >> Map(lambda x: (x, 1))
            | 'And sum by key' >> CombinePerKey(sum)
            | "Select top N" >> beam.combiners.Top.Largest(
                TOP_N, key=lambda x: x[1]
            )
            | 'Persist results' >> WriteToText('./results/q2/results.txt')
        )
