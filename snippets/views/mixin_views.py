from rest_framework import generics, mixins

from snippets.models import Snippets
from snippets.serializers import SnippetSerializer


class SnippetList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    """
    List or create code snippets.
    """

    queryset = Snippets.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)  # .list() is provided by mixins

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)  # .create() is provided by mixins


class SnippetDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    """
    Retrieve, update or delete code snippets.
    """

    queryset = Snippets.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)  # .retrieve() provided by mixins

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)  # .update() provided by mixins

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)  # .destroy() provide by mixins
