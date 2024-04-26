from django.urls import path
from . import views

app_name = "blogs"

urlpatterns = [
    path("", views.BlogListView.as_view(), name="blog-list"),
    path("blog/<slug:slug>/", views.BlogDetailView.as_view(), name="blog-detail"),
    path("blog/create/", views.BlogCreateView.as_view(), name="blog-create"),
    path(
        "blog/<slug:slug>/update/", views.BlogUpdateView.as_view(), name="blog-update"
    ),
    path(
        "blog/<slug:slug>/delete/", views.BlogDeleteView.as_view(), name="blog-delete"
    ),
    path(
        "blog/<slug:slug>/comment/",
        views.CommentCreateView.as_view(),
        name="comment-create",
    ),
    path(
        "blog/<slug:slug>/rate/", views.RatingCreateView.as_view(), name="rating-create"
    ),
]
