"""View module for handling requests for student data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from practicejournalapi.models import JournalEntry, Student, GuitarType


class JournalEntryView(ViewSet):
    """Honey Rae API journalentries view"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single journalEntry

        Returns:
            Response -- JSON serialized journalEntry record
        """

        journalentry = JournalEntry.objects.get(pk=pk)
        serialized = JournalEntrySerializer(
            journalentry, context={'request': request})

        return Response(serialized.data, status=status.HTTP_200_OK)

    def list(self, request):
        """Handle GET requests to get all journalentries

        Returns:
            Response -- JSON serialized list of journalentries
        """

        journalentries = JournalEntry.objects.all()
        serialized = JournalEntrySerializer(journalentries, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):
        """ Handle POST requests to create a new journal entry"""
        new_journalentry = JournalEntry()
        new_journalentry.student = Student.objects.get(
            pk=request.data["student"])
        new_journalentry.date_created = request.data['date']
        new_journalentry.time_created = request.data['time']
        new_journalentry.hours_slept = request.data['hoursSlept']
        new_journalentry.water = request.data['water']
        new_journalentry.nutrition = request.data['nutrition']
        new_journalentry.mood = request.data['mood']
        new_journalentry.description = request.data['description']
        new_journalentry.session_length = request.data['sessionLength']
        new_journalentry.guitar_type = request.data['guitartype']
        new_journalentry.save()

        serialized = JournalEntrySerializer(new_journalentry, many=False)

        return Response(serialized.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        """ Handle a PUT request to update a journal entry"""
        journalentry = JournalEntry.objects.get(pk=pk)
        guitartype = GuitarType.objects.get(pk=request.data['guitartypeId'])

        journalentry.hours_slept = request.data['hoursSlept']
        journalentry.water = request.data['water']
        journalentry.nutrition = request.data['nutrition']
        journalentry.mood = request.data['mood']
        journalentry.description = request.data['description']
        journalentry.session_length = request.data['sessionLength']
        journalentry.guitartype = guitartype

        journalentry.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class StudentJournalEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('id', 'full_name', 'age', 'style', 'years_playing')


class JournalEntrySerializer(serializers.ModelSerializer):
    """JSON serializer for journalentries"""
    student = StudentJournalEntrySerializer(many=False)

    class Meta:
        model = JournalEntry
        fields = ('id', 'student', 'date_created', 'time_created', 'hours_slept',
                  'water', 'nutrition', 'mood', 'description', 'session_length', 'guitartype')
        depth = 1
