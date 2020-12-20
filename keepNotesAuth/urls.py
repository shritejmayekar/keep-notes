from django.urls import path
from django.conf.urls import include
from keepNotesAuth import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from django.conf.urls import url

urlpatterns = [
    path('login/',views.login),
    path('register/',views.register),
    url('auth-jwt/', obtain_jwt_token),
    url('auth-jwt-refresh/', refresh_jwt_token),
    url('auth-jwt-verify/', verify_jwt_token),
]
