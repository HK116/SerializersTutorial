from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from snippets.views import (
    class_views,
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
    path("users/", class_views.UserList.as_view(), name="users"),
    path("users/<int:pk>", class_views.UserDetail.as_view(), name="user-details"),
    path("snippets/", class_views.SnippetList.as_view(), name="snippets"),
    path(
        "snippets/<int:pk>/",
        class_views.SnippetDetail.as_view(),
        name="snippet-details",
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
