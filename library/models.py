
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=100)
    comment = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    book_author = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    private = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})
