from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Comment(models.Model):
    full_name = models.CharField(max_length=1000)
    mail = models.EmailField(max_length = 1500)
    text = RichTextField()
    date = models.DateTimeField(auto_now_add = True , blank = True , null = True)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    
    def __str__(self):
        return self.full_name