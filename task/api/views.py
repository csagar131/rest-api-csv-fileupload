from django.shortcuts import render
from rest_framework import views
from rest_framework.parsers import FileUploadParser
from .serializers import FileUploaderSerializer
from .models import FileUploader
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# Create your views here.

class FileUploadView(views.APIView):
    parser_classes = (FileUploadParser,)
    serializer_class = FileUploaderSerializer
    queryset = FileUploader.objects.all()
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        file_obj = request.data['file']
        ser_data = FileUploaderSerializer(data = request.data)
        if ser_data.is_valid():
            print(request.data)
            print('------------------')
            print(file_obj)
            ser_obj =ser_data.save()
            return Response({'success':'ok'},status=204)
        # ...
        # do some stuff with uploaded file
        # ..
        return Response(ser_data.errors)