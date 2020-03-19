import pytest
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
