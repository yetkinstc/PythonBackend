from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=100)
    lastName=models.CharField(max_length=100)
    userName=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.name
    
class post(models.Model):
    #userId=models.ForeignKey(user,on_delete=models.CASCADE)
    userId=models.CharField(max_length=100)
    
    title=models.CharField(max_length=1000,default="")


