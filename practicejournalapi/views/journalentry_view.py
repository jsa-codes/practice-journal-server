"""View module for handling requests for student data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from practicejournalapi.models import JournalEntry


class JournalEntryView(ViewSet):
    """Honey Rae API journalentries view"""

    def list(self, request):
        """Handle GET requests to get all journalentries

        Returns:
            Response -- JSON serialized list of journalentries
        """

        journalentries = JournalEntry.objects.all()
        serialized = JournalEntrySerializer(journalentries, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single journalEntry

        Returns:
            Response -- JSON serialized journalEntry record
        """

        journalentry = JournalEntry.objects.get(pk=pk)
        serialized = JournalEntrySerializer(
            journalentry, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)


class JournalEntrySerializer(serializers.ModelSerializer):
    """JSON serializer for journalentries"""
    class Meta:
        model = JournalEntry
        fields = ('id', 'description', 'date', 'time')
        depth = 1
