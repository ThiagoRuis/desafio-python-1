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
            computed_skills = res.json['freelance']['computedSkills']
            expected_skills = [
                {'durationInMonths': 28, 'id': '241', 'name': 'React'},
                {'durationInMonths': 28, 'id': '270', 'name': 'Node.js'}, 
                {'durationInMonths': 28, 'id': '370', 'name': 'Javascript'}
            ]

            assert computed_skills == expected_skills
    
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
            computed_skills = res.json['freelance']['computedSkills']
            expected_skills = [
                {'durationInMonths': 28, 'id': '241', 'name': 'React'}, 
                {'durationInMonths': 28, 'id': '270', 'name': 'Node.js'}, 
                {'durationInMonths': 60, 'id': '370', 'name': 'Javascript'}, 
                {'durationInMonths': 32, 'id': '470', 'name': 'MySQL'}, 
                {'durationInMonths': 40, 'id': '400', 'name': 'Java'}
            ]
            assert computed_skills == expected_skills