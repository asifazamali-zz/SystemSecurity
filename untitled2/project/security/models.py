from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth import models
# Create your models here.

def get_upload_file_name(instance,filename):
    #print instance.author
    return "uploads/%s/%s" % (instance.user_name,filename)


class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    timestamp = models.DateTimeField(auto_now_add = True)       
class Document(models.Model):
    user_name = models.CharField(max_length=200)
    grantor = models.CharField(max_length=200,default='00000')
    docfile = models.FileField(upload_to=get_upload_file_name,default='00000')   
    read = models.BooleanField(default=1)
    write = models.BooleanField(default=0)
    owner = models.BooleanField(default=0)
    class Meta:
        db_table="documents"
    def __unicode__(self):
        return self.user_name
    
class Friends(models.Model):
    user_name=models.CharField(max_length=200)
    friend_name = models.CharField(max_length=200)
    
class Request_send(models.Model):
    user_name= models.CharField(max_length=200,default='00000')
    friend_req= models.CharField(max_length=200,default='00000')


class Shared(models.Model):
    user_name = models.CharField(max_length=200)
    docfile = models.CharField(max_length=200)   
    read = models.BooleanField(default=False)
    write = models.BooleanField(default=False)
    owner = models.BooleanField(default=False)
#class Request_recv(models.Model):
    #user_name= models.CharField(max_length=200,default='00000')
    #friend_req= models.CharField(max_length=200,default='00000')