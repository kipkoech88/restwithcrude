from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from .serializer import PostSerializer 
from base.models import Post 
from django.shortcuts import render

@api_view(['GET'])
def Posts(request):
    item=Post.objects.all() 
    serializer=PostSerializer(item, many=True)
    return Response(serializer.data) 

@api_view(['POST'])
def AddPost(request): 
    serializer=PostSerializer(data=request.data) 
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) 

@api_view(['PUT']) 
def PutPost(request):
    serializer=PostSerializer(data=request.data) 
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) 

def index(request):
    return render(request, 'base/index.html')