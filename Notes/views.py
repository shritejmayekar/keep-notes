from django.shortcuts import render
from Notes.models import Notes
from rest_framework import viewsets
from Notes.serializers import NoteSerializer
from rest_framework.response import Response
import django_filters
from django_filters.widgets import BooleanWidget

# Create your views here.


class NoteFilterSet(django_filters.FilterSet):

    class Meta:
        model = Notes
        fields = ['is_pinned', 'is_deleted','is_archieved','title','description']


class NoteViewset(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer
    filter_class = NoteFilterSet
    http_method_names = ['get', 'post', 'patch', 'delete']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(user=request.user)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
