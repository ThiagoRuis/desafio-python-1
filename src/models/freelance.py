from flask_restx import fields
from server.instance import server

from models.professional_experiences import professional_experience
from models.user import user

freelance = server.api.model('Freelance', {
    'id': fields.Integer(),
    'user': fields.Nested(user),
    'status': fields.String(required=True, min_length=1),
    'retribution': fields.Integer(),
    'availabilityDate': fields.String(required=True, min_length=1),
    'professionalExperience': fields.List(fields.Nested(professional_experience)),  
})