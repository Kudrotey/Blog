from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Headline(models.Model):
    headline_text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline_text

class Text(models.Model):
    headline = models.ForeignKey(Headline, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        if len(self.text) > 50:
            return f'{self.text[:50]}...'