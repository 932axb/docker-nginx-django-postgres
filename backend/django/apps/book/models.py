from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse


class PublishedManager(models.Manager):

    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Book(models.Model):
    """Books"""
    STATUS_CHOICE = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')

    objects = models.Manager()  # Default model manager
    published = PublishedManager()  # Custom model manager

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'book-detail',
            args=[
                self.slug
            ]
        )