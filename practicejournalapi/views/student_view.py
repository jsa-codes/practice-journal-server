"""View module for handling requests for student data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from practicejournalapi.models import Student


class StudentView(ViewSet):
    """Honey Rae API students view"""

    def list(self, request):
        """Handle GET requests to get all students

        Returns:
            Response -- JSON serialized list of students
        """

        students = Student.objects.all()
        serialized = StudentSerializer(students, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single student

        Returns:
            Response -- JSON serialized student record
        """

        student = Student.objects.get(pk=pk)
        serialized = StudentSerializer(student, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)

    # TO-DO: Create PUT request for editing student information:
        # age
        # style
        # years_playing
    def update(self, request, pk=None):
        guitartype = GuitarType.objects.get(pk=pk)
        student = Student.objects.get(pk=pk)

        student.age = request.data['age']
        student.style = request.data['style']
        student.years_playing = request.data['yearsPlaying']
        student.guitartype = guitartype

        guitartype.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    # TO-DO: Create DELETE request for deleting a student profile


class StudentSerializer(serializers.ModelSerializer):
    """JSON serializer for students"""
    class Meta:
        model = Student
        fields = ('id', 'user', 'age', 'style', 'years_playing', 'guitartype')
        depth = 3
