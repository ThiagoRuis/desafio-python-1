import pytest, json
from flask import url_for



class TestApp:

    def test_ping(self, client):
        res = client.get(url_for('ping'))
        assert res.status_code == 200
        assert res.json == {'ping': 'pong'}

    def test_root(self, client):
        res = client.get('/')
        assert res.status_code == 200
        assert res.json == {}

    def test_empty_entry(self, client):
        res = client.post('/', data={})
        assert res.status_code == 422

    def test_no_skills(self, client):
        mimetype = 'application/json'
        headers = {
            'Content-Type': mimetype,
            'Accept': mimetype
        }
        with open('examples/freelancer_no_skills.json') as json_file:
            data = json.load(json_file)
            res = client.post('/', json=dict(data), headers=headers)
            assert res.status_code == 422


    def test_single_experience_no_interval(self, client):
        mimetype = 'application/json'
        headers = {
            'Content-Type': mimetype,
            'Accept': mimetype
        }
        with open('examples/freelancer_experience_single_no_interval.json') as json_file:
            data = json.load(json_file)
            res = client.post('/', json=dict(data), headers=headers)
            assert res.status_code == 200

    # testar se existe skillName