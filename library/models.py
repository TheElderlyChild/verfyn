from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    """Model Representing a Course. 
    Example of courses: Books, Video Tutorial series, Program Collection
    """
    pass

class Chapter(models.Model):
    """Model Representing a collection of information about similar topics(Chapter)."""
    pass

class ContentUnit(models.Model):
    """Model Representing a collection of information about a topic.
    Example of ContentUnits include: Article, Blog Post, Video
    """
    pass

class Article(ContentUnit):
    """Information about a topic delivered without user feedback"""
    pass

class Post(ContentUnit):
    """Information about a topic with user feedback"""
    pass

class Comment(ContentUnit):
    """Model representing feedback from a User"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE) 
    text = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

class Segment(models.Model):
    """Model representing a segment of a content unit. Usually deals with a single concept."""
    pass

class Tag(models.Model):
    """Model representing a descriptor of content.
    Examples include: 'Funny', 'Art', 'NSFW'"""
    name = models.CharField(max_length=70, help_text='Enter a short descriptor (e.g. Thought Experiment)')


    #Methods
    def __str__(self):
        """String for representing the Model object."""
        return self.name