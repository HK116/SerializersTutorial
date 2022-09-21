from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND

from snippets.models import Snippets
from snippets.serializers import SnippetSerializer


@csrf_exempt
def snippet_list_create(request):
    """
    List or create code snippets.
    """

    if request.method == "GET":
        snippets = Snippets.objects.all()
        serializer = SnippetSerializer(snippets, many=True)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return JsonResponse(serializer.data, status=HTTP_200_OK)


@csrf_exempt
def snippet_details(request, pk):
    """
    Retrieve, update or delete code snippets.
    """
    try:
        snippet = Snippets.objects.get(pk=pk)
    except Snippets.DoesNotExist:
        raise HttpResponse(status=HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = SnippetSerializer(snippet)

        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return JsonResponse(serializer.data, status=HTTP_200_OK)

    elif request.method == "DELETE":
        snippet.delete()

        return JsonResponse(status=HTTP_204_NO_CONTENT)
