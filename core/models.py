from django.db import models

class Company(models.Model):
    name=models.CharField(max_length=200)
    website=models.URLField(blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    phone=models.CharField(max_length=20,blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    is_verified=models.BooleanField(default=False)
    

    def __str__(self):
        return self.name