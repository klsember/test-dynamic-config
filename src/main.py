# -*- coding: utf-8 -*-

import requests

SAMPLE_SERVICE_URL = "https://httpbin.org/get"

def read_service_as_json(url):
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    json_response = read_service(SAMPLE_SERVICE_URL)
    print(json_response)