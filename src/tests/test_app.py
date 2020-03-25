import pytest, json

from controller import *
from utils import compute_time, compute_skills

class TestApp:
    def test_empty_entry(self, client):
        mimetype = 'application/json'
        headers = {
            'Content-Type': mimetype,
            'Accept': mimetype
        }
        res = client.post('/freelance', json={}, headers=headers)
        assert res.status_code == 400

    def test_no_skills(self, client):
        mimetype = 'application/json'
        headers = {
            'Content-Type': mimetype,
            'Accept': mimetype
        }
        with open('./examples/freelancer_no_skills.json') as json_file:
            data = json.load(json_file)
            res = client.post('/freelance', json=dict(data), headers=headers)
            assert res.status_code == 400


    def test_single_experience_no_interval(self, client):
        mimetype = 'application/json'
        headers = {
            'Content-Type': mimetype,
            'Accept': mimetype
        }
        with open('./examples/freelancer_experience_single_no_interval.json') as json_request:
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
        with open('./examples/freelancer.json') as json_request:
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

    def test_compute_time(self, client):
        first_interval = {
            "start": "2016-01-01",
            "end": "2016-05-01"
        }

        buffer = compute_time(first_interval['start'], first_interval['end'], [])
        expected_response = ['2016-01', '2016-02', '2016-03', '2016-04']
        assert sorted(buffer) == (expected_response)
        assert len(buffer) == 4

        second_interval = {
            "start": "2018-01-01",
            "end": "2018-05-01"
        }

        response = compute_time(second_interval['start'], second_interval['end'], buffer)
        expected_response = ['2016-01', '2016-02', '2016-03', '2016-04', '2018-01', '2018-02', '2018-03', '2018-04']
        assert sorted(response) == (expected_response)
        assert len(response) == 8