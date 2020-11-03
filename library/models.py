from django.db import models
from django.urls import reverse

# Create your models here.
class Course(models.Model):
    pass

class Chapter(models.Model):
    pass

class ContentUnit(models.Model):
    pass

class Article(ContentUnit):
    pass

class Post(ContentUnit):
    pass

class Section(models.Model):
    pass

class Tag(models.Model):
    pass