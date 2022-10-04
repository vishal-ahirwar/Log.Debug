from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

#model for storing Post status
class Status(models.TextChoices):
    #enum
    DRAFT='DF','Draft'
    PUBLISHED='PB','Published'

#model for storing user posts
class Post(models.Model):
    #Attributes
    Author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Post')
    Title=models.CharField(max_length=250)
    Slug=models.CharField(max_length=250)
    Body=models.TextField()
    Publish=models.DateTimeField(default=timezone.now)
    Created=models.DateTimeField(auto_now_add=True)
    Updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=2,choices=Status.choices,default=Status.DRAFT)

    #class
    class Meta:
        #order of filtering data from database
        ordering=['-Publish']
        #database index to improve the performance for queries filtering|ordering
        indexes=[
            models.Index(fields=['-Publish']),
        ]

    #methods
    def __str__(self):
        return self.Title

