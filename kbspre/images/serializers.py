from rest_framework import serializers
from . import models

class CommentSerializer(serializers.ModelSerializer):
    #    image = ImageSerializer()
    class Meta:
        model = models.Comment
        #fields = '__all__'
        fields =(
            #'id',
            #'created_at',
            'playername',
            #'step',
            'score',
            #'tel',
            #'mail',
            #'survey',
            #'note',
        )
        
class LikeSerializer(serializers.ModelSerializer):
    #    image = ImageSerializer()
    class Meta:
        model = models.Like
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    likes = LikeSerializer(many=True)
    class Meta:
        model = models.Image
    #   fields ='__all__'
        fields =(
            'id',
            'file',
            'location',
            'caption',
            'comments',
            'likes'
        )
