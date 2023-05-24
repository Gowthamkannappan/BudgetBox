
from rest_framework.response import Response
from rest_framework import status

def error_response(message, status_code):
    response_data = {
        'error': message
    }
    return Response(response_data, status=status_code)
