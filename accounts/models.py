import uuid
from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save
from PIL import Image
from posts.upload_paths import upload_post_image
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    birth_day = models.DateTimeField(null=True,blank=True)
    bio = models.TextField()
    image = models.ImageField(blank=True,upload_to=upload_post_image)
    slug = models.SlugField(editable=False)

    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.user.username)
            self.slug = f"{base}-{uuid.uuid4().hex[:6]}"
        super().save(*args, **kwargs)

        if self.image:
            img = Image.open(self.image.path)
            if img.height > 200 and img.width > 200:
                new_size = (200,200)
                img.thumbnail(new_size)
                img.save(self.image.path)

    def __str__(self):
        return self.user.username
    
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile,sender=settings.AUTH_USER_MODEL)