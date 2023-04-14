from django.db import models



# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    body = models.TextField(blank=True)
    
    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    body = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
class Institute(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.name
    
class EdSource(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    body = models.TextField(blank=True)
    institute = models.ManyToManyField(Institute, blank=True, related_name='edsources')

    def __str__(self):
        return self.title
    
    
class Person(models.Model):
    first_name = models.CharField(max_length=255,blank=True)
    last_name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    institute = models.ManyToManyField(Institute, blank=True,related_name='persons')
    videos = models.ManyToManyField(Video,blank=True, related_name='persons')

    def __str__(self):
        return self.last_name
    

    
    
class Work(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Person,blank=True, related_name='works')
    summary = models.TextField()
    videos = models.ManyToManyField(Video,blank=True,related_name='works')

    def __str__(self):
        return self.title
    
class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(Person,blank=True, related_name='teams')
    works = models.ManyToManyField(Work,blank=True, related_name='teams')
    introduction = models.TextField(blank=True)
    institute = models.ManyToManyField(Institute,blank=True,related_name="teams")
    link = models.URLField(blank=True)

    def __str__(self):
        return self.name
    
class Discipline(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    key_figures = models.ManyToManyField(Person,blank=True, related_name='disciplines')
    introduction = models.TextField()
    parents = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='disciplines')
    works = models.ManyToManyField(Work, blank=True, related_name='disciplines')
    research_teams = models.ManyToManyField(Team,blank=True,related_name='disciplines')
    news = models.ManyToManyField(News, blank=True, related_name='disciplines')
    sources = models.ManyToManyField(EdSource, blank=True, related_name='disciplines')
    videos = models.ManyToManyField(Video, blank=True, related_name='disciplines')
    def __str__(self):
        return self.title