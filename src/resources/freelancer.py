from flask import Flask
from flask_restx import Api, Resource, fields

from models.freelancer import freelancer
from server.instance import server

app, api = server.app, server.api


@api.route('/freelancer')
class FreelancerList(Resource):
    # Ask flask_restplus to validate the incoming payload
    @api.expect(freelancer, validate=True)
    @api.marshal_with(freelancer)
    def get(self):
        
        return api.payload