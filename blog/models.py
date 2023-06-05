from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=120)

    def __str__(self):
          return self.name   

 


class Article(models.Model):
    title = models.CharField(max_length=50)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    desc = models.TextField()
    image = models.ImageField()
    created_at=models.DateField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
       return self.title    

class Test(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    image = models.ImageField()
    
    