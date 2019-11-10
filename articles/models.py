from django.db import models
from django.urls import reverse
# Create your models here.

class Article(models.Model):
	article_title=models.CharField(max_length=100)
	article_description=models.TextField()


	def get_absolute_url(self):
		# f"/article_details_display/{self.id}/"
		return reverse("article-details-display-id", kwargs={"pass_id": self.id})

	def get_absolute_url_delete(self):
		return reverse("article-details-delete-id", kwargs={"pass_id": self.id})
		#return f"/article_details_delete/{self.id}/"


	def get_absolute_url_edit(self):
		#return f"/article_edit/{self.id}/"
		return reverse("article-edit-id", kwargs={"pass_id": self.id})


	def get_guest_absolute_url_view(self):
		return reverse("guest_article-details-display-id", kwargs={"pass_id": self.id})
