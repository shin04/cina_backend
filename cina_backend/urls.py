from django.contrib import admin
from django.urls import include, path

from userinfo.urls import router as userinfo_router
from timemanagement.urls import router as tm_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/user_info/', include(userinfo_router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),

    path('api/v1/timemanagement/', include(tm_router.urls)),
]
