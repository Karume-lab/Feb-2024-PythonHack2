from django.urls import path
from . import views

app_name = "blogs"

urlpatterns = [
    path("", views.BlogListView.as_view(), name="blog-list"),
    path("/<slug:slug>/", views.BlogDetailView.as_view(), name="blog-detail"),
    path("/create/", views.BlogCreateView.as_view(), name="blog-create"),
    path(
        "/<slug:slug>/update/", views.BlogUpdateView.as_view(), name="blog-update"
    ),
    path(
        "/<slug:slug>/delete/", views.BlogDeleteView.as_view(), name="blog-delete"
    ),
    path(
        "/<slug:slug>/comment/",
        views.CommentCreateView.as_view(),
        name="comment-create",
    ),
    path(
        "/<slug:slug>/rate/", views.RatingCreateView.as_view(), name="rating-create"
    ),
]
