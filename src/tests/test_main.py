# -*- coding: utf-8 -*-

import pytest

def test_load_main():
    from src import main

def test_read_service_as_json():
    from src import main
    sample_service_url = "https://httpbin.org/get"
    response_json = main.read_service_as_json(sample_service_url)
    response_host = response_json['headers']['Host']
    assert response_host == 'httpbin.org'