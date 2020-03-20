from flask import Flask, jsonify, request, Response
from datetime import datetime

def create_app():
    app = Flask(__name__)

    @app.route('/ping')
    def ping():
        return jsonify(ping='pong')

    @app.route('/', methods=['POST'])
    def freelancer_evaluate():
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
        

    @app.route('/', methods=['GET'])
    def main():
        return jsonify()

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

    #todo: REFATORE !!!
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

    #todo: REFATORE !!!
    def compute_time(start_date, end_date, buffer):
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        
        while start != end:
            buffer.setdefault(start.strftime('%Y-%m'))
            start = datetime(start.year + int(start.month / 12), (start.month % 12) + 1, 1)
        return buffer

    return app




        


if __name__ == '__main__':
    app = create_app()
    app.run(port=5000)