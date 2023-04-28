from django.db import models

class Categories(models.Model):
    category_name = models.CharField(max_length=50)
    def __str__(self):
        return self.category_name
class Post(models.Model):
    heading = models.CharField(max_length=255)
    short_paragraph = models.CharField(max_length=300)
    cover_image = models.ImageField(upload_to='media')
    story = models.TextField()
    date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    writer = models.CharField(max_length=50)
    def __str__(self):
        return self.heading
    
class Comments(models.Model):
    comment = models.TextField()
    comment_user = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now=True)
# Create your models here.
