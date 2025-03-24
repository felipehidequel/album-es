from django.contrib.auth import authenticate
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from user.models import Photographer
from user.api import PhotographerSerializer, LoginSerializer


class PhotographerViewSet(viewsets.ModelViewSet):
    queryset = Photographer.objects.all()
    serializer_class = PhotographerSerializer
    permission_classes = [permissions.IsAuthenticated]

class LoginAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if not serializer.is_valid():                       
            return Response({
                "status" : False,
                "data" : serializer.errors
            })
        
        username = serializer.data['username']
        password = serializer.data['password']

        user_obj = authenticate(username = username, password = password)
        if user_obj:
            token , _ =Token.objects.get_or_create(user=user_obj)
            return Response({
                "status" : True,
                "data" : {'token' : str(token)}
            })

        
        return Response({
                "status" : False,
                "data" : {},
                "message" : "Credentials invalid"
            })
