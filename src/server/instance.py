from flask import Flask
from flask_restx import Api, Resource, fields
from environment.instance import environment_config

class Server(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app, 
            version='1.0', 
            title='Evaluation API',
            description='A simple freelancer evaluation API', 
            doc = environment_config["swagger-url"]
        )

    def run(self):
        self.app.run(
                debug = environment_config["debug"], 
                port = environment_config["port"]
            )

server = Server()