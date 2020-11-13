from rest_framework import serializers

from questions.models import Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'question']
        depth = 2