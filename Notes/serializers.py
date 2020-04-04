from rest_framework import serializers
from notes.models import Notes


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        exclude = ('user',)

    def create(self, validated_data):
        note = Notes.objects.create(
            title=validated_data['title'],
            description=validated_data['description'],
            user=self.context['request'].user
        )
        return note
