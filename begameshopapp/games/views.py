from rest_framework.viewsets import ModelViewSet
from .serializers import *

# Create your views here.


class GameViewSet(ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
