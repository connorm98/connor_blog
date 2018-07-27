from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ("title", "slug", "author", "status", "created")

	#http://muva.co.ke/blog/lesson-5-creating-administration-site-for-our-blog-models-in-django-1-11-4-and-python-3-5/


admin.site.register(Post)