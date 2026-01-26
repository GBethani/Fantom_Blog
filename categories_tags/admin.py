from django.contrib import admin
from . import models
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_filter = ['title']
    list_display = ['slug',]
    search_fields = ['title','body']

    class Meta:
        model = models.Category

admin.site.register(models.Category,CategoryAdmin)
