"""View module for handling requests for instructor data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from practicejournalapi.models import Instructor


class InstructorView(ViewSet):
    """Honey Rae API instructors view"""

    def list(self, request):
        """Handle GET requests to get all instructors

        Returns:
            Response -- JSON serialized list of instructors
        """

        instructors = Instructor.objects.all()
        serialized = InstructorSerializer(instructors, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single instructor

        Returns:
            Response -- JSON serialized instructor record
        """
        instructor = Instructor.objects.get(pk=pk)
        serialized = InstructorSerializer(
            instructor, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        """ Handle PUT requests for single instructor"""
        instructor = Instructor.objects.get(pk=pk)

        instructor.age = request.data['age']
        instructor.years_playing = request.data['yearsPlaying']
        instructor.bio = request.data['bio']
        instructor.location = request.data['location']

        instructor.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for single instructor"""
        instructor = Instructor.objects.get(pk=pk)
        instructor.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class InstructorSerializer(serializers.ModelSerializer):
    """JSON serializer for instructors"""
    class Meta:
        model = Instructor
        fields = ('id', 'age',
                  'years_playing', 'bio', 'location')
        depth = 3