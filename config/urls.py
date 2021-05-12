from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

auth_urls = [
    path('get-token/', obtain_jwt_token),
    path('refresh-token/', refresh_jwt_token),
    path('verify-token/', verify_jwt_token),
]

# API URLS
urlpatterns += [
    path('api/auth/', include(auth_urls)),
    path("api/", include("config.api_router")),
]
