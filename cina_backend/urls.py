from django.contrib import admin
from django.urls import include, path

from posts.urls import router as posts_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(posts_router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
]
