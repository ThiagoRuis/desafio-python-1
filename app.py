from flask import Flask, jsonify, request, Response
from flask_restplus import Resource, Api
from datetime import datetime

app = Flask(__name__)
api = Api(app)

class Evaluation(Resource):
    def post(self):
        data = request.json
        code = validate(data)
        if not code is None:
            return Response(status=code)
        skillset = {}
        for experience in data['freelance']['professionalExperiences']:
            for skill in experience['skills']:
                skillname = f"{skill['id']}-{skill['name']}" 
                period = {
                    'startDate': experience['startDate'].split('T')[0],
                    'endDate': experience['endDate'].split('T')[0],
                }
                skillset.setdefault(skillname, []).append(period)

        computed_skills = compute_skills(skillset)
        evaluation = {
            "freelance": {
                "id": data['freelance']['id'],
                "computedSkills": computed_skills
            }
        }
        return jsonify(evaluation)

    def validate(request_body):
        wrong_format_code = 422
        if request_body is None or request_body == '' or request_body == {}:
            return wrong_format_code
        
        # Check format
        if not 'freelance' in request_body:
            return wrong_format_code

        if not 'professionalExperiences' in request_body['freelance']:
            return wrong_format_code
        
        if len(request_body['freelance']['professionalExperiences']) < 1:
            return wrong_format_code
        
        for experience in request_body['freelance']['professionalExperiences']:
            if not 'skills' in experience:
                return wrong_format_code

        pass

    def compute_skills(skillset):
        computed_skills = []
        for skill in skillset:
            computed_time = {}
            id, name = skill.split('-')
            for period in skillset[skill]:
                computed_time = compute_time(period['startDate'], period['endDate'], computed_time)

            computed_skills.append({
                "id": id,
                "name": name,
                "durationInMonths": len(computed_time)
            })
            
        return computed_skills

    def compute_time(start_date, end_date, buffer):
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        
        while start != end:
            buffer.setdefault(start.strftime('%Y-%m'))
            start = datetime(start.year + int(start.month / 12), (start.month % 12) + 1, 1)
        return buffer


if __name__ == '__main__':
    app.run(debug=True, port=5000)