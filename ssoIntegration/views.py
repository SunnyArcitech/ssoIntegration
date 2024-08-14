from rest_framework.response import Response
from rest_framework.views import APIView
from google.oauth2 import id_token
from google.auth.transport import requests
from rest_framework import status
from ssoIntegration.settings import GOOGLE_CLIENT_IDS
import time

class GoogleSingin(APIView):
    def post(self, request):
        data = request.data.copy()
        token = data['id_token']
        idinfo = None
        try:
            # Verifying if sent token is valid and belongs to any legit gmail user   
            idinfo = id_token.verify_oauth2_token(token, requests.Request())
            
            if not idinfo:
                raise ValueError('Invalid token.')
            
            if idinfo['aud'] not in GOOGLE_CLIENT_IDS:
                raise ValueError(f'Could not verify audience {idinfo["aud"]}')
            
            if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise ValueError('Wrong issuer.')
            
            if idinfo['exp'] < time.time():
                raise ValueError('Token has expired.')

        except Exception as e:
            print(e)
            return Response(
                {
                    "error": "error",
                    "message": "Invalid Token"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # If the token is valid, Do the user registration or handle login flow 
        return Response(
            {
                "status": "success",
                "message": "Valid Token",
                'created': 'Done'
            },
            status=status.HTTP_200_OK
        )

