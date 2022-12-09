"""View module for handling requests for student data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from practicejournalapi.models import Audio


class AudioView(ViewSet):
    """Honey Rae API audios view"""

    def list(self, request):
        """Handle GET requests to get all audios

        Returns:
            Response -- JSON serialized list of audios
        """

        audio = Audio.objects.all()
        serialized = AudioSerializer(audio, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single audio

        Returns:
            Response -- JSON serialized audio record
        """

        audio = Audio.objects.get(pk=pk)
        serialized = AudioSerializer(audio, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):
        new_audio = Audio()
        new_audio.student = Student.objects.get(
            pk=request.data["student"])
        new_audio.date_created = request.data['date']
        new_audio.time_created = request.data['date']
        new_audio.save()

        serialized = JournalEntrySerializer(new_audio, many=False)

        return Response(serialized.data, status=status.HTTP_201_CREATED)


class AudioSerializer(serializers.ModelSerializer):
    """JSON serializer for audios"""
    class Meta:
        model = Audio
        fields = ('id', 'filename', 'date')
        depth = 1
