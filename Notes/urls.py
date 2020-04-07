from Notes import views
from rest_framework import routers
from django.conf.urls import url, include


v1_router = routers.DefaultRouter()

v1_router.register(r'note', views.NoteViewset)

urlpatterns = [
    url(r'v1/', include(v1_router.urls))

]
