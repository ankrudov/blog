from rest_framework import serializers
from .models import BlogPost

#serializers turn the querydate into readable datatypes by javascript and front end framework
class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
        lookup_field = 'slug'
