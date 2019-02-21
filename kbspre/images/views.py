from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers


class ListAllImages(APIView):
    def get(self, request, format=None):
        all_images = models.Image.objects.all()
        serializer = serializers.ImageSerializer(all_images, many=True)
        return Response(data=serializer.data)

class ListAllLikes(APIView):
    def get(self, request, format=None):
        all_Likes = models.Like.objects.all()
        serializer = serializers.LikeSerializer(all_Likes, many=True)
        return Response(data=serializer.data)

class ListAllComments(APIView):
    def get(self, request, format=None):
        all_Comments = models.Comment.objects.all()
        serializer = serializers.CommentSerializer(all_Comments, many=True)
        return Response(data=serializer.data)
    
    #class Meta:
    #    ordering = ['-created_at']

'''
class ListAllComments(APIView):
    def get(self, request, format=None):
        all_Comments = models.Comment.objects.filter(step=1)
        serializer = serializers.CommentSerializer(all_Comments, many=True)
        return Response(data=serializer.data)
'''

class ListSfComments(APIView):
    def get(self, request, format=None):
        sf_Comments = models.Comment.objects.filter(step=1).order_by('-score')[:3]
        serializer = serializers.CommentSerializer(sf_Comments, many=True)
        return Response(data=serializer.data) 

class ListRfComments(APIView):
    def get(self, request, format=None):
        rf_Comments = models.Comment.objects.filter(step=1)[:5]
        serializer = serializers.CommentSerializer(rf_Comments, many=True)
        return Response(data=serializer.data)
        
class ListSsComments(APIView):
    def get(self, request, format=None):
        ss_Comments = models.Comment.objects.filter(step=2).order_by('-score')[:3]
        serializer = serializers.CommentSerializer(ss_Comments, many=True)
        return Response(data=serializer.data)
        
class ListRsComments(APIView):
    def get(self, request, format=None):
        rs_Comments = models.Comment.objects.filter(step=2)[:5]
        serializer = serializers.CommentSerializer(rs_Comments, many=True)
        return Response(data=serializer.data)
        
class ListStComments(APIView):
    def get(self, request, format=None):
        st_Comments = models.Comment.objects.filter(step=3).order_by('-score')[:3]
        serializer = serializers.CommentSerializer(st_Comments, many=True)
        return Response(data=serializer.data)
        
class ListRtComments(APIView):
    def get(self, request, format=None):
        rt_Comments = models.Comment.objects.filter(step=3)[:5]
        serializer = serializers.CommentSerializer(rt_Comments, many=True)
        return Response(data=serializer.data)