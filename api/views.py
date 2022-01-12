from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes
from api.serializers import RegisterSerializer
from rest_framework import generics



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

