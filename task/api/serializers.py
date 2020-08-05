from rest_framework import serializers
from .models import FileUploader
import os

class FileUploaderSerializer(serializers.ModelSerializer):
    # overwrite = serializers.BooleanField()
    class Meta:
        model = FileUploader
        fields = ('file','name','upload_date')
        read_only_fields = ('name','upload_date')
    
    def validate(self, validated_data):
        validated_data['name'] = os.path.splitext(validated_data['file'].name)[0]
        # print('getting here')
        # print(validated_data['file'])
        file_type = os.path.splitext(validated_data['file'].name)[1]
        validated_data['file_type'] = file_type
        file_path = 'media/files'
        validated_data['file_path'] = file_path
        if file_type != '.csv':
            raise serializers.ValidationError("file should be csv")
        return validated_data

    def create(self, validated_data):
        return FileUploader.objects.create(**validated_data)

