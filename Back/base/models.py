from django.db import models
from django.contrib.auth.models import User

class AllBooks(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    desc = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')
    genre = models.CharField(max_length=50, null=True, blank=True)
    author = models.CharField(max_length=50, null=True, blank=True)
    createdTime=models.DateTimeField(auto_now_add=True)
    _id=models.AutoField(primary_key=True,editable=False)
    def __str__(self):
        return self.title

class Loans(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey(AllBooks, on_delete=models.SET_NULL, null=True)
    createdTime=models.DateTimeField(auto_now_add=True)
    _id=models.AutoField(primary_key=True,editable=False)
    def __str__(self):
        return self.title