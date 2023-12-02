import os
import json
import requests

def ocr_space_url(url, api_key):
    """ OCR.space API request with URL """
    payload = {
        'url': url,
        'isOverlayRequired': True,
        'apikey': api_key,
        'language': 'eng',
    }
    response = requests.post('https://api.ocr.space/parse/image',
                             data=payload,
                            )
    return response.json()

def ocr_function(request):
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'file_paths' in request_json:
        file_paths = request_json['file_paths']
    elif request_args and 'file_paths' in request_args:
        file_paths = request_args['file_paths']
    else:
        return 'No file paths provided', 400

    if not isinstance(file_paths, list):
        return 'file_paths must be a list', 400
    api_key = os.environ.get('OCR_API_KEY', 'K89921444488957')  # Set your OCR.space API key in environment variables

    all_text_results = []

    for file_path in file_paths:
        result = ocr_space_url(file_path, api_key)
        text_results = [res['ParsedText'] for res in result['ParsedResults']]
        all_text_results.append('\n'.join(text_results))
    print(all_text_results)

    return json.dumps(all_text_results)