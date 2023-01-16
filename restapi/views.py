'''
This file contains views for the Django REST API. Each view is decorated with the @api_view decorator, which specifies the HTTP methods that the view will handle.
The login view is used to handle user login requests. It uses the AuthTokenSerializer to validate the incoming request data and create an authentication token for the user. The user's data is then serialized using the serialize_user function and returned as a response along with the token.
The register view is used to handle user registration requests. It uses the RegisterSerializer defined in the serializers.py file to validate and create a new user account. After the account is created, an authentication token is created and returned in the response along with the user's data.
The get_user view is used to retrieve the currently authenticated user's information. It checks whether the user is authenticated and returns a response containing the user's data if they are, or an empty response if they are not.
The knox package is used for handling authentication and token management. The AuthToken class is used to create authentication tokens for the API. The TokenAuthentication class is used to authenticate users based on tokens.
The serialize_user is a helper function used to convert the user instance into a serializable format (Dictionary).
'''

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken, TokenAuthentication
from .serializers import RegisterSerializer

def serialize_user(user):
    return {
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name
    }

@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    _, token = AuthToken.objects.create(user)
    return Response({
        'user_data': serialize_user(user),
        'token': token
    })
        

@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        _, token = AuthToken.objects.create(user)
        return Response({
            "user_info": serialize_user(user),
            "token": token
        })


@api_view(['GET'])
def get_user(request):
    user = request.user
    if user.is_authenticated:
        return Response({
            'user_data': serialize_user(user)
        })
    return Response({})