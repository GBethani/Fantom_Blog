from django.shortcuts import render
from django.db.models import Count
from django.views.generic import ListView,DetailView
from posts.models import Post
from categories_tags.models import Category
import random


class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"
    context_object_name = "posts"
    paginate_by = 6
    ordering = ["-published_at"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 1️⃣ Get UNIQUE post IDs only (guaranteed unique by DB)
        post_ids = list(
            Post.objects.values_list("id", flat=True)
        )

        # 2️⃣ Shuffle in Python (not DB)
        random.shuffle(post_ids)

        # 3️⃣ Select first 10 UNIQUE IDs
        slider_ids = post_ids[:10]

        # 4️⃣ Fetch posts (still unique)
        context["slider_posts"] = (
            Post.objects
            .filter(id__in=slider_ids)
            .distinct()
        )

        context["categories"] = Category.objects.annotate(
            post_count=Count("post")
        )

        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = "post"

