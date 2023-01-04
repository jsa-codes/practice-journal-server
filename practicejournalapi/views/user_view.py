from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from practicejournalapi.models import Student
from practicejournalapi.models import Instructor


class UserView(ViewSet):
    """Honey Rae API users view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single student

        Returns:
            Response -- JSON serialized student record
        """
        if pk == "current":
            user = request.user
            if user.is_staff:
                instructor = Instructor.objects.get(user=user)

                data = {
                    "id": instructor.id,
                    "firstName": user.first_name,
                    "lastName": user.last_name,
                    "bio": instructor.bio,
                    "style": instructor.style
                }
            else:
                student = Student.objects.get(user=user)

                data = {
                    "id": student.id,
                    "age": student.age,
                    "firstName": user.first_name,
                    "lastName": user.last_name,
                    "style": student.style,
                    "yearsPlaying": student.years_playing,
                }
            return Response(data, status=status.HTTP_200_OK)

    def list(self, request):
        """Handle GET requests for all users """
        if request.user.is_staff:
            instructor = Instructor.objects.get(user=request.user)

            data = {
                "id": instructor.id,
                "firstName": instructor.first_name,
                "lastName": instructor.last_name,
            }
            return Response(data, status=status.HTTP_200_OK)
