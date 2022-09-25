from typing import ClassVar
from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from snippets.views.class_views import (
    api_root,
    UserList,
    UserDetail,
    SnippetList,
    SnippetDetail,
    SnippetHighlight,
)
from snippets.views import (
    regular_views,
    mixin_views,
    wrapper_views,
)

# urlpatterns = [
#     path("snippets/", regular_views.snippet_list, name="snippets"),
#     path("snippets/<int:pk>/", regular_views.snippet_detail, name="snippet-details"),
# ]

# urlpatterns = [
#     path("snippets/", wrapper_views.snippet_list, name="snippets"),
#     path("snippets/<int:pk>/", wrapper_views.snippet_detail, name="snippet-details"),
# ]

# urlpatterns = [
#     path("snippets/", mixin_views.SnippetList.as_view(), name="snippets"),
#     path("snippets/<int:pk>/", mixin_views.SnippetDetail.as_view(), name="snippet-details"),
# ]

urlpatterns = [
    path("", api_root),
    path("users/", UserList.as_view(), name="user-list"),
    path("users/<int:pk>/", UserDetail.as_view(), name="user-detail"),
    path("snippets/", SnippetList.as_view(), name="snippet-list"),
    path("snippets/<int:pk>/", SnippetDetail.as_view(), name="snippets-detail"),
    path(
        "snippets/<int:pk>/highlight/",
        SnippetHighlight.as_view(),
        name="snippet-highlight",
    ),
]


urlpatterns = format_suffix_patterns(urlpatterns)
