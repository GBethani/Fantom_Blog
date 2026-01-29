from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from .models import Category
from .querysets import categories_with_post_count
from posts.models import Post

class CategoryPostListView(ListView):
    model = Post
    template_name = "categories_tags/categ.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        # 1️⃣ Get category slug from URL
        self.category = get_object_or_404(
            Category,
            slug=self.kwargs["slug"]
        )

        # 2️⃣ Return posts related to this category
        return Post.objects.filter(
            categories=self.category
        ).order_by("-published_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 3️⃣ Pass category to template
        context["category"] = self.category

        # 4️⃣ Count posts in this category
        context["post_count"] = self.category.post_set.count()

        return context


class CategoryListView(ListView):
    model = Category
    template_name = 'categories_tags/category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return categories_with_post_count()
