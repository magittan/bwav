import requests
import json
import time

API_KEY = "Bearer 01jS3bvO2rL7OS0_GRmF-Z7h77p1Cp1RF_3se_E5_9brna0XdVV8_prQjeut-2HOEIG1WzFQLrwfJ5Q9bjHXiL66bkVEg"
HEADERS = {'Authorization': API_KEY}

def submit_job_url(media_url):
    url = "https://api.rev.ai/revspeech/v1beta/jobs"
    payload = {'media_url': media_url,
               'metadata': "Test"}
    request = requests.post(url, headers=HEADERS, json=payload)

    if request.status_code != 200:
        raise

    response_body = request.json()
    return response_body['id']

def submit_job_file(file):
    url = "https://api.rev.ai/revspeech/v1beta/jobs"
    files = { 'media': (file, open(file, 'rb'), 'audio/mp3') }
    request = requests.post(url, headers=HEADERS, files=files)
    if request.status_code != 200:
        raise

    response_body = request.json()
    return response_body['id']

def view_job(id=59594172):
    url = f'https://api.rev.ai/revspeech/v1beta/jobs/{id}'
    request = requests.get(url, headers=HEADERS)

    if request.status_code != 200:
        raise

    response_body = request.json()
    return response_body

def get_transcript(id='59594172'):
    url = f'https://api.rev.ai/revspeech/v1beta/jobs/{id}/transcript'
    headers = HEADERS.copy()
    headers['Accept'] = 'application/vnd.rev.transcript.v1.0+json'
    request = requests.get(url, headers=headers)

    if request.status_code != 200:
        print("error", request.status_code)
        raise

    response_body = request.json()
    parse(response_body)
    return response_body

def parse(response_body):
    stringReader = []
    for element in response_body['monologues'][0]['elements']:
        stringReader += element['value']
    print(''.join(stringReader))

def test_workflow_with_url(url):
    print ("Submitting job with URL")
    id = submit_job_url(url)
    print ("Job created")
    print(id)
    view_job(id)

    while True:
        job = view_job(id)
        status = job["status"]
        print (f'Checking job transcription status: { status }')
        if status == "transcribed":
            break
        if status == "failed":
            raise

        print ("Trying in another 10 seconds")
        time.sleep(10)

    return get_transcript(id)

def test_workflow_with_file(file):
    print ("Submitting job with file")
    id = submit_job_file(file)
    print ("Job created")
    view_job(id)

    while True:
        job = view_job(id)
        status = job["status"]
        print (f'Checking job transcription status: { status }')
        if status == "transcribed":
            break
        if status == "failed":
            raise

        print ("Trying in another 30 seconds")
        time.sleep(30)

    return get_transcript(id)

def main():
    # Testing with URL
    media_url = "https://support.rev.com/hc/en-us/article_attachments/200043975/FTC_Sample_1_-_Single.mp3"
    test_workflow_with_url(media_url)

    # Testing with file upload
    # file = "test.mp3"
    # test_workflow_with_file(file)

if __name__ == "__main__":
    main()