from flask import Flask, jsonify, request, Response


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
        pass

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
        
        pass

    return app


        


if __name__ == '__main__':
    app = create_app()
    app.run(port=5000)