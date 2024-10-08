from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    source = models.CharField(null=True,max_length=100)
    likes = models.IntegerField(default=0)

class Comment(models.Model):
    article= models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
       return f"Comment by{self.user} on {self.article}"
   
   
   
    def __str__(self):
     return self.title





