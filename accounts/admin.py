from django.contrib import admin
from . import models
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_filter = ['user']
    list_display = ['slug',]
    search_fields = ['bio',]

    class Meta:
        model = models.UserProfile

admin.site.register(models.UserProfile,UserProfileAdmin)