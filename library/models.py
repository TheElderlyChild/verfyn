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
    """Model Representing a collection of articles about similar topics(Chapter)."""
    pass

class Article(models.Model):
    """Model Representing a collection of information about a topic.
    It could be anything from an essay to a video.
    """
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    description = models.TextField()

    created = models.DateTimeField(default=timezone.now) #When the article was first created
    updated = models.DateTimeField(null=True,blank=True) #The most recent edit to the article
    published = models.DateTimeField(null=True,blank=True) #When the article was made available to the public
   
    isPublished = models.BooleanField(default=False)
    view_count = models.IntegerField(_("View count"), default=0)

    #Methods
    def __str__(self):
        "String for representing the post"
        return self.title + " by " + self.author

class Comment(models.Model):
    """Model representing feedback from a User"""
    article = models.ForeignKey(Article, on_delete=models.CASCADE) 
    text = models.TextField(max_length=500)
    timestamp = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    #Methods
    def __str__(self):
        """String for representing a Comment."""
        return 'Comment at ' + str(self.timestamp) + ' by '+ str(self.author) + " on " + self.article

class Segment(models.Model):
    """Model representing a segment of an article. Usually deals with a single concept."""
    pass

class Tag(models.Model):
    """Model representing a descriptor of content.
    Examples include: 'Funny', 'Art', 'NSFW'"""
    name = models.CharField(max_length=70, help_text='Enter a short descriptor (e.g. Thought Experiment)')


    #Methods
    def __str__(self):
        """String for representing a Tag."""
        return self.name