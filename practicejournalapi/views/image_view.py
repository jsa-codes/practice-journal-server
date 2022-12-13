"""View module for handling requests for student data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from practicejournalapi.models import Image


class ImageView(ViewSet):
    """Honey Rae API images view"""

    def list(self, request):
        """Handle GET requests to get all images

        Returns:
            Response -- JSON serialized list of images
        """

        images = Image.objects.all()
        serialized = ImageSerializer(images, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single image

        Returns:
            Response -- JSON serialized image record
        """

        image = Image.objects.get(pk=pk)
        serialized = ImageSerializer(image, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):
        """ Handle POST requests for single image"""
        new_image = Image()
        new_image.student = Student.objects.get(
            pk=request.data["student"])
        new_image.date_created = request.data['date']
        new_image.time_created = request.data['time']
        new_image.save()

        serialized = JournalEntrySerializer(new_image, many=False)

        return Response(serialized.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        """ Handle PUT requests for single image"""

        image = Image.objects.get(pk=pk)
        image.filename = request.data['filename']

        image.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    # Create a DELETE request for deleting an image
    def destroy(self, request, pk=None):
        image = Image.objects.get(pk=pk)
        image.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class ImageSerializer(serializers.ModelSerializer):
    """JSON serializer for images"""
    class Meta:
        model = Image
        fields = ('id', 'filename', 'date')
        depth = 1
