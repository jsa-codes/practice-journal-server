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

        student = Student.objects.get(user=request.auth.user)
        guitartype = GuitarType.objects.get(pk=request.data['guitartypeId'])

        journalentry = JournalEntry.objects.create(
            date_created=request.data['date'],
            time_created=request.data['time'],
            hours_slept=request.data['hoursSlept'],
            water=request.data['water'],
            nutrition=request.data['nutrition'],
            mood=request.data['mood'],
            description=request.data['description'],
            session_length=request.data['sessionLength'],
            guitartype=guitartype,
            student=student
        )

        serializer = JournalEntrySerializer(journalentry)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

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
                  'water', 'nutrition', 'mood', 'description', 'session_length', 'guitartype', 'comments')
        depth = 1
