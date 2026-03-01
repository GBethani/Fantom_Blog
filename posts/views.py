from django.shortcuts import render
from django.db.models import Count, Q
from django.views.generic import ListView,DetailView
from posts.models import Post
from categories_tags.models import Category
import random


class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"
    context_object_name = "posts"
    paginate_by = 6
    # ordering = ["-published_at"]

    # def get_queryset(self):
    #     """
    #     If user is staff:
    #         Show ALL posts (including drafts)
    #     Else:
    #         Show only published posts
    #     """

    #     if self.request.user.is_staff:
    #         # Admin/staff users see everything
    #         return Post.objects.all().order_by("-published_at")

    #     # Normal users see only published posts
    #     return Post.published.all().order_by("-published_at")
    def get_queryset(self):
        return Post.visible_to(self.request.user).order_by("-published_at")
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 1️⃣ Get UNIQUE post IDs only (guaranteed unique by DB)
        # if self.request.user.is_staff:
        #     post_ids = list(Post.objects.values_list("id", flat=True))
        # else:
        #     post_ids = list(Post.published.values_list("id", flat=True))
        post_ids = list(Post.visible_to(self.request.user).values_list("id", flat=True))

        # 2️⃣ Shuffle in Python (not DB)
        random.shuffle(post_ids)

        # 3️⃣ Select first 10 UNIQUE IDs
        slider_ids = post_ids[:10]

        # 4️⃣ Fetch posts (still unique)
        context["slider_posts"] = (
            Post.published
            .filter(id__in=slider_ids)
        )

        context["categories"] = Category.objects.annotate(
            post_count=Count("post", filter=Q(post__status="published"))
        )

        return context

class PostDetailView(DetailView):

    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = "post"

    def get_queryset(self):
        if self.request.user.is_staff:
            return Post.objects.all()
        return Post.published.all()

