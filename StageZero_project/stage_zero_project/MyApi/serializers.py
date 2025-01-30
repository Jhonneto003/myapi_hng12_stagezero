from rest_framework import serializers

class MyApiSerializer(serializers.Serializer):
    email = serializers.EmailField()
    github_url = serializers.URLField()
    current_datetime = serializers.DateTimeField()