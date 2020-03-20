from flask_restx import fields
from server.instance import server

freelancer = server.api.model('Skill', {
    'id': fields.Integer(description='Id'),
    'name': fields.String(required=True, min_length=1, description='Skill name'),
    
})