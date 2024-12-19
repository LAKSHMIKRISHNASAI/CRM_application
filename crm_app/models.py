from django.db import models


class Record(models.Model):

    #datetime,firstname,lastname,email,phone, addrress.
    creation_time=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=100)

    email=models.EmailField(max_length=255)
    phone=models.CharField(max_length=10)
    city=models.CharField(max_length=100)
    province=models.CharField(max_length=100)
    country=models.CharField(max_length=100)

    def __str__(self):
        return self.first_name+' '+self.last_name
    
