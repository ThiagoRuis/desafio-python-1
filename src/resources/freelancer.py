from flask import Flask, jsonify, request, Response
from flask_restx import Api, Resource, fields
from datetime import datetime

from models.freelance import freelance
from server.instance import server

app, api = server.app, server.api


@api.route('/freelance')
class FreelancerList(Resource):
    def compute_skills(self, skillset):
        computed_skills = []
        for skill in skillset:
            computed_time = {}
            id, name = skill.split('-')
            for period in skillset[skill]:
                computed_time = compute_time(start_date=period['startDate'], end_date=period['endDate'], buffer=computed_time)

            computed_skills.append({
                "id": id,
                "name": name,
                "durationInMonths": len(computed_time)
            })
            
        return computed_skills

    def compute_time(self, start_date, end_date, buffer):
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        
        while start != end:
            buffer.setdefault(start.strftime('%Y-%m'))
            start = datetime(start.year + int(start.month / 12), (start.month % 12) + 1, 1)
        return buffer

    # Ask flask_restplus to validate the incoming payload
    @api.expect(freelance, validate=True)
    @api.marshal_with(freelance)
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
        return jsonify(evaluation)