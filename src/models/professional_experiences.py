from flask_restx import fields
from server.instance import server
from models.skill import skill

professional_experience = server.api.model('ProfessionalExperience', {
    'id': fields.Integer(description='Id'),
    'companyName': fields.String(required=True, min_length=1, description='Company name of the job'),
    'startDate':  fields.String(required=True, min_length=1, description='Start date of the job'),
    'endDate':  fields.String(required=True, min_length=1, description='End date of the job'),
    'skills':  fields.List(fields.Nested(skill))    
})