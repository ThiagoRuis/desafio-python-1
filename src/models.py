from flask_restx import fields
from server.instance import server

user = server.api.model('User', {
    'firstName': fields.String(required=True, min_length=1, description='User first name'),
    'lastName': fields.String(required=True, min_length=1, description='User last name'),
    'jobTitle': fields.String(required=True, min_length=1, description='User title'),
})

skill = server.api.model('Skill', {
    'id': fields.Integer(description='Id'),
    'name': fields.String(required=True, min_length=1, description='Skill name'),
    
})

professional_experience = server.api.model('ProfessionalExperience', {
    'id': fields.Integer(description='Id'),
    'companyName': fields.String(required=True, min_length=1, description='Company name of the job'),
    'startDate':  fields.String(required=True, min_length=1, description='Start date of the job'),
    'endDate':  fields.String(required=True, min_length=1, description='End date of the job'),
    'skills':  fields.List(fields.Nested(skill))    
})

job = server.api.model('Job', {
    'id': fields.Integer(required=True),
    'user': fields.Nested(user),
    'status': fields.String(),
    'retribution': fields.Integer(),
    'availabilityDate': fields.String(),
    'professionalExperiences': fields.List(fields.Nested(professional_experience)),  
})

freelance = server.api.model('Freelance', {
    'freelance': fields.Nested(job)
})