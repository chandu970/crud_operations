from django.db import models

# Create your models here.

class Topic(models.Model):
    topic=models.CharField(max_length=100,primary_key=True)
    
    def __str__(self):
        return self.topic
    
class Webpage(models.Model):
    topic=models.ForeignKey(Topic, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()
    
    def __str__(self):
        return self.name
    
class AccessRecords(models.Model):
    name=models.ForeignKey(Webpage, on_delete=models.CASCADE)
    athour=models.CharField(max_length=100)
    date=models.DateField()
     
    def __str__(self):
        return self.athour
