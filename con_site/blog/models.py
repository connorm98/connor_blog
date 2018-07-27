from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#Our blog post model

class Post(models.Model):
	STATUS_CHOICES = (
		("draft", "Draft"),
		("published", "Published"),
	)
	# blog post title
	title = models.CharField(max_length=250)

	#  slug is how we generate a uniuque url for the post
	slug = models.SlugField(max_length=250, unique_for_date="publish")

	# Post authors name
	author = models.ForeignKey(User, related_name="blog_posts")

	# Post content
	body = models.TextField()

	# indicates the time the post was published
	publish = models.DateTimeField(default=timezone.now)

	# indicates the time the post was created
	created = models.DateTimeField(auto_now_add=True)

	# indicates the time the post was last updated
	updated = models.DateTimeField(auto_now=True)

	#shows the status of the post (published or draft)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")

	class Meta:

		# this tells django to sort by the publish field in descending order (most recent first)
		ordering = ("-publish",)

		def __str__(self):
			# this presents the object in a human readable format.
			return self.title