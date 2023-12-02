import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions,GoogleCloudOptions,SetupOptions
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
def run():
    pipeline_options = PipelineOptions(
        runner='DataflowRunner',
        project='reliable-bruin-403416',
        temp_location='gs://cotiviti-cliical-notes/temp',
        region='us-central1',
        requirements_file='requirements.txt')
    
    with beam.Pipeline(options=pipeline_options) as pipeline:
        (pipeline
         | 'Read File Paths' >> beam.Create(['https://storage.googleapis.com/cotiviti-cliical-notes/Group-Therapy-Progress-Note-Example.png'])  # Replace with actual file paths or source
         | 'Call OCR Function' >> beam.ParDo(CallOCRFunction())
         | 'Write to Firestore' >> beam.ParDo(WriteToFirestore())
        )

if __name__ == '__main__':
    run()