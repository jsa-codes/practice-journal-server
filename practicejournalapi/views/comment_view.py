"""View module for handling requests for student data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from practicejournalapi.models import Comment


class CommentView(ViewSet):
    """Honey Rae API comments view"""

    def list(self, request):
        """Handle GET requests to get all comments

        Returns:
            Response -- JSON serialized list of comments
        """

        comments = Comment.objects.all()
        serialized = CommentSerializer(comments, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single comment

        Returns:
            Response -- JSON serialized comment record
        """

        comment = Comment.objects.get(pk=pk)
        serialized = CommentSerializer(comment, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):
        new_comment = Comment()
        new_comment.student = Student.objects.get(
            pk=request.data["student"])
        new_comment.date_created = request.data['date']
        new_comment.time_created = request.data['time']
        new_comment.save()

        serialized = JournalEntrySerializer(new_comment, many=False)

        return Response(serialized.data, status=status.HTTP_201_CREATED)


class CommentSerializer(serializers.ModelSerializer):
    """JSON serializer for comments"""
    class Meta:
        model = Comment
        fields = ('id', 'description', 'date', 'time')
        depth = 1
