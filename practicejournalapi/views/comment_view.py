"""View module for handling requests for student data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from practicejournalapi.models import Comment, JournalEntry


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
        """ Handle POST requests for single comment"""
        user = User.objects.get(id=request.auth.user.id)
        journalentry = JournalEntry.objects.get(
            pk=request.data['journalentryId'])

        comment = Comment.objects.create(
            date_created=request.data['date'],
            time_created=request.data['time'],
            description=request.data['description'],
            user=user,
            journalentry=journalentry
        )

        serializer = CommentSerializer(comment)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        """ Handle PUT requests for a single comment. """
        comment = Comment.objects.get(pk=pk)
        comment.description = request.data['description']

        comment.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

        # Create a DELETE request for comments


class CommentSerializer(serializers.ModelSerializer):
    """JSON serializer for comments"""
    class Meta:
        model = Comment
        fields = ('id', 'description', 'date_created', 'time_created')
        depth = 1
