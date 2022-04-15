from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets

from .models import PostModel
from .serializers import PostSerializer

# Create your views here.
#1
class PostViewSet(viewsets.ModelViewSet):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer

# #2 
# class ListPost(generics.ListCreateAPIView):
#     queryset = PostModel.objects.all()
#     serializer_class = PostSerializer

# class DetailPost(generics.RetrieveUpdateDestroyAPIView):
#     queryset = PostModel.objects.all()
#     serializer_class = PostSerializer