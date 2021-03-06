from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from begameshopapp.users.views import UserViewSet
from begameshopapp.games.views import *

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("games", GameViewSet)
router.register("categories", CategoryViewSet)
router.register("reviews", ReviewViewSet)

app_name = "api"
urlpatterns = router.urls
