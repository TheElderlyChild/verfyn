from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    """Model representing a descriptor of content.
    Examples include: 'Funny', 'Art', 'NSFW'"""
    name = models.CharField(max_length=70, help_text='Enter a short descriptor (e.g. Thought Experiment)')


    #Methods
    def __str__(self):
        """String for representing a Tag."""
        return self.name
        
class Course(models.Model):
    """Model Representing a Course. 
    Example of courses: Books, Video Tutorial series, Program Collection
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    description = models.TextField()
    outline = models.TextField()
    tag = models.ManyToManyField(Tag, help_text='Descriptive tags for this course')

    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    #Methods
    def __str__(self):
        "String for representing the course"
        return self.title  
    
    def incLikes(self):
        """Increases the number of likes of the course"""
        self.likes += 1

    def incDislikes(self):
        """Increases the number of dislikes of the course"""

    @property
    def tableOfContents(self):
        """Generates the Table Of Contents of the Course"""
        pass

class Chapter(models.Model):
    """Model Representing a collection of articles about similar topics(Chapter)."""
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    description = models.TextField()

    
    intro = models.TextField(null=True, blank=True)
    summary = models.TextField()

    #Methods
    def __str__(self):
        "String for representing the chapter"
        return self.title  
    

class Article(models.Model):
    """Model Representing a collection of information about a topic.
    It could be anything from an essay to a video.
    """
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    description = models.TextField()

    created = models.DateTimeField(default=timezone.now) #When the article was first created
    updated = models.DateTimeField(null=True,blank=True) #The most recent edit to the article
    published = models.DateTimeField(null=True,blank=True) #When the article was made available to the public
   
    viewCount = models.IntegerField(default=0)

    position = models.AutoField()

    class Meta:
        ordering = ("position")

    #Methods
    def __str__(self):
        "String for representing the article"
        return self.title

    def incViews(self):
        """Increases the view count of the article"""
        self.viewCount += 1

    @property
    def isPublished(self):
        """returns True only if the article has been published"""
        return (self.published != None)


    def publish(self):
        """Publishes the article for view in the Chapter"""
        if not self.isPublished:
            self.published = timezone.now()

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
    
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    header = models.CharField(max_length=200)
    content = models.TextField()
    position = models.AutoField()

    class Meta:
        ordering = ("position")

