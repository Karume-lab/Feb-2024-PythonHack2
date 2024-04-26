from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from . import models


class BlogListView(ListView):
    model = models.Blog
    template_name = "blogs/blog_list.html"
    context_object_name = "blogs"


class BlogDetailView(DetailView):
    model = models.Blog
    template_name = "blogs/blog_detail.html"
    context_object_name = "blog"


class BlogCreateView(CreateView):
    model = models.Blog
    template_name = "blogs/blog_form.html"
    fields = ["title", "content", "image"]
    success_url = reverse_lazy("blogs:blog-list")


class BlogUpdateView(UpdateView):
    model = models.Blog
    template_name = "blogs/blog_form.html"
    fields = ["title", "content", "image"]
    success_url = reverse_lazy("blogs:blog-list")


class BlogDeleteView(DeleteView):
    model = models.Blog
    template_name = "blogs/blog_confirm_delete.html"
    success_url = reverse_lazy("blogs:blog-list")


class CommentCreateView(CreateView):
    model = models.Comment
    template_name = "blogs/comment_form.html"
    fields = ["content"]
    success_url = reverse_lazy("blogs:blog-list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog = models.Blog.objects.get(slug=self.kwargs["slug"])
        return super().form_valid(form)


class RatingCreateView(CreateView):
    model = models.Rating
    template_name = "blogs/rating_form.html"
    fields = ["rating"]
    success_url = reverse_lazy("blogs:blog-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.blog = models.Blog.objects.get(slug=self.kwargs["slug"])
        return super().form_valid(form)
