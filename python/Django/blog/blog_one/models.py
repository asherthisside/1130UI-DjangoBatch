from django.db import models
from datetime import datetime

# Create your models here.
class Blog(models.Model):
    blog_picture = models.ImageField(null=True)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=20)
    description = models.TextField()
    created_at = models.DateTimeField(default=datetime.now())
    author = models.CharField(max_length=20, default="Admin")

    def __str__(self):
        return f"{self.id} - {self.title}"
