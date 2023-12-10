# Interoperability Technology for Health Care: Leveraging Cloud-Native Solutions

## Project Overview
This project focuses on automating text extraction from clinical notes using OCR.space hosted on Google Cloud Function. It involves a Dataflow pipeline for processing image paths and utilizing cloud functions for text extraction, storing data in Google Cloud Firestore. It's a practical application of interoperability technology in healthcare.

## Analysis of Current Trends and Relevance
The project aligns with current healthcare trends emphasizing data interoperability for improved patient care and operational efficiency, offering a scalable cloud-native solution for processing healthcare data.

## Advantages and Opportunities
- **Scalability and High Availability:** Utilizes cloud services for resource scaling and performance.
- **Global Accessibility:** Facilitates collaborative and flexible development.
- **Enhanced Security:** Ensures robust security for sensitive healthcare data.

## Code Overview
1. **Dataflow Pipeline Template (`dataflow_pipeline_template.py`):** Creates a pipeline template for image path processing and OCR text extraction.
2. **Dataflow Pipeline Runner (`dataflow_pipeline_runner.py`):** Executes the dataflow job, automating complex data processing.
3. **Cloud Function for Dataflow Template Runner (`CF_dataflow_template_runner.py`):** Triggers the Dataflow pipeline, demonstrating cloud service integration.
4. **OCR Text Extractor Cloud Function (`CF_ocr_text_extractor.py`):** Extracts text from images using the OCR.space API.

## Strategic Recommendations for Cotiviti
Exploring investments in similar cloud-native solutions to enhance data processing capabilities, including partnerships with technology providers or developing in-house cloud-based ETL/ELT processes expertise.


![Blank diagram (1)](https://github.com/nikhilattili/Cotiviti-clinical-notes/assets/29622506/1376a30b-31d5-4f23-94ff-a9d80796126f)


## References
- [Google Cloud Dataflow - Creating Templates](https://cloud.google.com/dataflow/docs/guides/templates/creating-templates#metadataparameters)
- [Google Cloud Scheduler - HTTP Target Authentication](https://cloud.google.com/scheduler/docs/http-target-auth)
- [Triggering Cloud Run with Cloud Scheduler](https://cloud.google.com/run/docs/triggering/using-scheduler)
- [Cloud Function to Start a Dataflow Job on File Upload](https://medium.com/@aishwarya.gupta3/cloud-function-to-start-a-data-flow-job-on-a-new-file-upload-in-google-cloud-storage-using-trigger-30270b31a06d)
- [Google Cloud Functions - Console Quickstart](https://cloud.google.com/functions/docs/console-quickstart)
