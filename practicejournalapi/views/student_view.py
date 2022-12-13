"""View module for handling requests for student data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from practicejournalapi.models import Student, GuitarType


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

    def update(self, request, pk=None):
        """ Handle PUT requests for single student"""
        student = Student.objects.get(pk=pk)
        instructor = User.objects.get(pk=request.data['instructorId'])
        guitartype = GuitarType.objects.get(pk=request.data['guitartypeId'])

        student.age = request.data['age']
        student.style = request.data['style']
        student.years_playing = request.data['yearsPlaying']
        student.guitartype = guitartype
        student.instructor = instructor

        student.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for single student"""
        student = Student.objects.get(pk=pk)
        student.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class StudentSerializer(serializers.ModelSerializer):
    """JSON serializer for students"""
    class Meta:
        model = Student
        fields = ('id', 'user', 'age', 'style',
                  'years_playing', 'guitartype', 'instructor')
        depth = 3
