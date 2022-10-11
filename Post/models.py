from dataclasses import fields
from email.policy import default
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
    Slug=models.CharField(max_length=250,unique_for_date='Publish')
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

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=80)
    mail=models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    class Meta:
        ordering=['-created']
        indexes=[
            models.Index(fields=['-created']),
        ]
        def __str__(self):
            return f"Comment by {self.name} on {self.post}"


