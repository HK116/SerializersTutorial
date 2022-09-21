from django.urls import path

from snippets.views import snippet_list_create, snippet_details

urlpatterns = [
    path("snippets/", snippet_list_create, name="snippets"),
    path("snippets/<int:pk>/", snippet_details, name="details"),
]
