from flask import Flask, jsonify, request, Response
from flask_restx import Api, Resource, fields, ValidationError

from models import freelance
from server.instance import server
from utils import compute_skills

app, api = server.app, server.api


@api.route('/freelance')
class FreelancerList(Resource):
    @api.expect(freelance, validate=True)
    def post(self):
        data = request.json
        skillset = {}
        for experience in data['freelance']['professionalExperiences']:
            for skill in experience['skills']:
                skillname = f"{skill['id']}-{skill['name']}" 
                period = {
                    'startDate': experience['startDate'].split('T')[0],
                    'endDate': experience['endDate'].split('T')[0],
                }
                skillset.setdefault(skillname, []).append(period)

        computed_skills = compute_skills(skillset=skillset)
        evaluation = {
            "freelance": {
                "id": data['freelance']['id'],
                "computedSkills": computed_skills
            }
        }
        return evaluation, 200