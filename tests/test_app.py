import pytest, json
from flask import url_for
from resources.freelancer import *

class TestApp:
    def test_empty_entry(self, client):
        res = client.post('/freelance', json={})
        assert res.status_code == 422

    def test_no_skills(self, client):
        mimetype = 'application/json'
        headers = {
            'Content-Type': mimetype,
            'Accept': mimetype
        }
        with open('examples/freelancer_no_skills.json') as json_file:
            data = json.load(json_file)
            res = client.post('/freelance', json=dict(data), headers=headers)
            assert res.status_code == 400


    def test_single_experience_no_interval(self, client):
        mimetype = 'application/json'
        headers = {
            'Content-Type': mimetype,
            'Accept': mimetype
        }
        with open('examples/freelancer_experience_single_no_interval.json') as json_request:
            data = json.load(json_request)
            res = client.post('/freelance', json=dict(data), headers=headers)
            assert res.status_code == 200
            with open('examples/freelancer_experience_single_no_interval_response.json') as json_response:
                assert res.json == json.load(json_response)
    
    def test_full_example(self, client):
        mimetype = 'application/json'
        headers = {
            'Content-Type': mimetype,
            'Accept': mimetype
        }
        with open('examples/freelancer.json') as json_request:
            data = json.load(json_request)
            res = client.post('/freelance', json=dict(data), headers=headers)
            assert res.status_code == 200
            #with open('examples/freelancer_experience_single_no_interval_response.json') as json_response:
            #    assert res.json == json.load(json_response)
    