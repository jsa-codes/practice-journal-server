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


class AudioSerializer(serializers.ModelSerializer):
    """JSON serializer for audios"""
    class Meta:
        model = Audio
        fields = ('id', 'filename', 'date')
        depth = 1
