"""View module for handling requests for student data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from practicejournalapi.models import GuitarType


class GuitarTypeView(ViewSet):
    """Honey Rae API guitartypes view"""

    def list(self, request):
        """Handle GET requests to get all guitartypes

        Returns:
            Response -- JSON serialized list of guitartypes
        """

        guitartypes = GuitarType.objects.all()
        serialized = GuitarTypeSerializer(guitartypes, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single guitartype

        Returns:
            Response -- JSON serialized guitartype record
        """

        guitartype = GuitarType.objects.get(pk=pk)
        serialized = GuitarTypeSerializer(
            guitartype, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)

        # TO-DO: Implement a PUT function for editing the guitartype:
        # acoustic
        # electric
    def update(self, request, pk=None):
        """ Handle PUT requests for updating guitar type"""
        guitartype = GuitarType.objects.get(pk=pk)
        guitartype.type = request.data['guitartype']

        guitartype.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        # TO-DO: Implement a DELETE function for deleting the guitartype

    # TO-DO
        # Create a DELETE request for deleting an audio upload


class GuitarTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for guitartypes"""
    class Meta:
        model = GuitarType
        fields = ('id', 'type')
        depth = 1
