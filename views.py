from rest_framework import status, viewsets, generics
from rest_framework.decorators import api_view
from serializers import *
from django.contrib.auth.models import User


class tasklist(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def list(self, request):
        if not request.user.is_superuser:
            queryset = self.queryset.all().filter(username=request.user)
        else:
            queryset = self.queryset.all()
        serializer = SnippetSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(username=self.request.user.username)


class detailtasklist(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


@api_view(['GET'])
def snippet_search(request, search):
    if request.method == 'GET':
        snippets = Snippet.objects.all().filter(desc=search)
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)
