from flask_restx import fields
from server.instance import server

user = server.api.model('User', {
    'firstName': fields.String(required=True, min_length=1, description='User first name'),
    'lastNamme': fields.String(required=True, min_length=1, description='User last name'),
    'jobTitle': fields.String(required=True, min_length=1, description='User title'),
})