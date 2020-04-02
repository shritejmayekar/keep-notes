from django.urls import path
from django.conf.urls import include
from keepNotesAuth import views
urlpatterns = [
    path('login/',views.login),
    path('register/',views.register)
]
