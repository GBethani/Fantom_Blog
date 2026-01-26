from django.utils.text import slugify
from django.core.management.base import BaseCommand
from faker import Faker
from posts.models import Post
from categories_tags.models import Category
import random

faker = Faker()

class Command(BaseCommand):
    
    help = "assign categories to n number of posts"

    def add_arguments(self, parser):
        parser.add_argument('--posts',type=int,default=25,help="number of posts to update")
        parser.add_argument('--catg',type=int,default=2,help="number o categories to assign")
        parser.add_argument('--replace',action="store_true",help="replace existing categories")

    def handle(self, *args, **options):
        post_count = options['posts']
        catg_count = options['catg']
        replace = options['replace']

        posts = Post.objects.order_by('?')[:post_count]
        categories = list(Category.objects.all())

        if not posts.exists():
            self.stdout.write(self.style.ERROR("No posts found"))
            return

        if not categories:
            self.stdout.write(self.style.ERROR("No categories found"))
            return
        
        for post in posts:
            selected = random.sample(categories,min(catg_count,len(categories)))

            if replace:
                post.categories.set(selected)
            else:
                post.categories.add(*selected)

        self.stdout.write(
                self.style.SUCCESS(
                    f"Assigned categories to {posts.count()} posts"
                )
            )