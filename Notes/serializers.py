from rest_framework import serializers
from Notes.models import Notes


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        exclude = ('user',)

    def create(self, validated_data):
        validated_data['user']=self.context['request'].user
        note = Notes.objects.create(**validated_data)
        return note
