from googleapiclient.discovery import build
import google.auth
import time
import json

def startDataflowProcess(request):
	from googleapiclient.discovery import build
	project = "reliable-bruin-403416"
	job = project + " " + str(time.time())
 
	#path of the dataflow template on google storage bucket
	template = "gs://cotiviti-cliical-notes/templates/ocr-citiviti-v2"

	#tempLocation is the path on GCS to store temp files generated during the dataflow job
	environment = {'tempLocation': 'gs://cotiviti-cliical-notes/temp/'}

	service = build('dataflow', 'v1b3', cache_discovery=False)
	#below API is used when we want to pass the location of the dataflow job
	request = service.projects().locations().templates().launch(
		projectId=project,
		gcsPath=template,
		location='us-central1',
		body={
			'jobName': job,
			'environment':environment
		},
	)
	response = request.execute()
	print(str(response))
	return json.dumps({"message": "Function executed successfully"}), 200