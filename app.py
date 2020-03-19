from flask import Flask, jsonify, request, Response


def create_app():
    app = Flask(__name__)

    @app.route('/ping')
    def ping():
        return jsonify(ping='pong')

    @app.route('/', methods=['POST'])
    def freelancer_evaluate():
        freelance = request.json
        code = validate(freelance)
        if not code is None:
            return Response(status=code)
        pass
        

    @app.route('/', methods=['GET'])
    def main():
        return jsonify()

    def validate(request_body):
        print(request_body)
        if request_body is None or request_body == '' or request_body == {}:
            print('CARAIO')
            return 422
        

    return app


        


if __name__ == '__main__':
    app = create_app()
    app.run(port=5000)