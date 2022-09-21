from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from snippets.views import snippet_list_create, snippet_details

urlpatterns = [
    path("snippets/", snippet_list_create, name="snippets"),
    path("snippets/<int:pk>/", snippet_details, name="details"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
