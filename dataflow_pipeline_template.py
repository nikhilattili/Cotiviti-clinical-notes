import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, GoogleCloudOptions, SetupOptions, ValueProvider
import logging

class CallOCRFunction(beam.DoFn):
    def process(self, element):
        import requests
        # Replace with your Cloud Function URL
        cloud_function_url = 'https://us-central1-reliable-bruin-403416.cloudfunctions.net/cotiviti-gen1-ocr'

        response = requests.post(cloud_function_url, json={"file_paths": [element]})
        if response.status_code == 200:
            result = response.json()
            return [(element, result)]
        else:
            return [(element, response.status_code)]

class WriteToFirestore(beam.DoFn):
    def start_bundle(self):
        from google.cloud import firestore
        self.db = firestore.Client()

    def process(self, element):
        file_path, ocr_result = element
        doc_ref = self.db.collection(u'ocr_results').document()  # You can customize your collection name
        doc_ref.set({
            u'file_path': file_path,
            u'ocr_result': ocr_result
        })

class RuntimeOptions(PipelineOptions):
    @classmethod
    def _add_argparse_args(cls, parser):
        parser.add_value_provider_argument(
            '--input_file',
            type=str,
        help='Path to the input file to process')

def run(argv=None):
    pipeline_options = PipelineOptions(
        argv,
        runner='DataflowRunner',
        project='reliable-bruin-403416',
        temp_location='gs://cotiviti-cliical-notes/temp',
        region='us-central1',
        template_location='gs://cotiviti-cliical-notes/templates/ocr-citiviti-v2',
        requirements_file='requirements.txt')

    runtime_options = pipeline_options.view_as(RuntimeOptions)

    with beam.Pipeline(options=pipeline_options) as pipeline:
        (pipeline
         | 'Read File Paths' >> beam.Create(['https://storage.googleapis.com/cotiviti-cliical-notes/Group-Therapy-Progress-Note-Example.png'])
         | 'Call OCR Function' >> beam.ParDo(CallOCRFunction())
         | 'Write to Firestore' >> beam.ParDo(WriteToFirestore())
        )

if __name__ == '__main__':
    run()