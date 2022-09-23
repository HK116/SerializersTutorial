from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from snippets.models import Snippets
from snippets.serializers import SnippetSerializer


@api_view(["GET", "POST"])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == "GET":
        snippets = Snippets.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippets.objects.get(pk=pk)
    except Snippets.DoesNotExist:
        return Response({"Snippet doesn't exist!"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
