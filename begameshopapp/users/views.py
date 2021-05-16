from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from begameshopapp.users.serializers import UserSerializer
from .models import User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
