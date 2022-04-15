from rest_framework import serializers
from .models import PostItem

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostItem
        fields = (
            'id',
            'title',
            'content',
        )
        # fileds = '__all__'

        
            