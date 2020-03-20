from flask import Flask
from flask_restx import Api, Resource, fields

from models.freelance import freelance
from server.instance import server

app, api = server.app, server.api


@api.route('/freelance')
class FreelancerList(Resource):
    # Ask flask_restplus to validate the incoming payload
    @api.expect(freelance, validate=True)
    @api.marshal_with(freelance)
    def get(self):
        
        return api.payload