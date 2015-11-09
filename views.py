from rest_framework import status
from rest_framework.decorators import api_view
from serializers import *
from django.contrib.auth.models import User


@api_view(['GET', 'POST'])
def snippet_list(request):
    if request.method == 'GET':
        if not request.user.is_superuser:
            snippet = Snippet.objects.all().filter(username=request.user)
        else:
            snippet = Snippet.objects.all()
        serializer = SnippetSerializer(snippet, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk):
    try:
        snippet = Snippet.objects.get(id=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_410_GONE)


@api_view(['GET'])
def snippet_search(request, search):
    if request.method == 'GET':
        snippets = Snippet.objects.all().filter(desc=search)
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

