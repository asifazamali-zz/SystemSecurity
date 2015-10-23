from django.db import models
import os
from django.contrib.auth.models import User
#from django.contrib.auth import models
# Create your models here.

def get_upload_file_name(instance,filename):
    #print instance.author
    return "uploads/%s/%s" % (instance.user_name,filename)
def dummy_function(instance,filename):
    #print instance.author
    return

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
    privacy = models.CharField(default='0',max_length='2')
    class Meta:
        db_table="documents"
    def filename(self):
        #print os.path.basename(self.docfile.name)
        return os.path.basename(self.docfile.name)

class Friends(models.Model):
    user_name=models.CharField(max_length=200)
    friend_name = models.CharField(max_length=200)


    
class Request_send(models.Model):
    user_name= models.CharField(max_length=200,default='00000')
    friend_req= models.CharField(max_length=200,default='00000')
    document_name = models.FileField(upload_to=dummy_function,default='00000')
    class Meta:
        db_table="request_send"


class Shared(models.Model):
    user_name = models.CharField(max_length=200)
    docfile = models.CharField(max_length=200)   
    read = models.BooleanField(default=False)
    write = models.BooleanField(default=False)
    owner = models.BooleanField(default=False)

class Details(models.Model):
    user_name = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    phnumber = models.CharField(max_length=200)
    email = models.EmailField()
    class Meta:
        db_table="profile_details"

class PrivacyDetails(models.Model):
    user_name = models.CharField(max_length=200)
    name = models.CharField(max_length=2)
    age = models.CharField(max_length=2)
    location = models.CharField(max_length=2)
    phnumber = models.CharField(max_length=2)
    email = models.EmailField()
    class Meta:
        db_table="profile_privacy"

class PrivacyFriend(models.Model):
    user_name = models.CharField(max_length=200)
    privacy = models.CharField(max_length=2)
    class Meta:
        db_table="friend_privacy"

class PrivacyDocs(models.Model):
    user_name = models.CharField(max_length=200)
    docfile = models.FileField(upload_to=dummy_function,default='00000')
    privacy = models.CharField(max_length=2,default='0')
    class Meta:
        db_table = "document_privacy"

class Question(models.Model):
    question = models.CharField(max_length=200)
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)
    option_correct = models.CharField(max_length=2)
    class Meta:
        db_table='questions'

class Answer(models.Model):
    user_name = models.CharField(max_length=500)
    question_id = models.CharField(max_length=2)
    answer = models.CharField(max_length=2)
    class Meta:
        db_table='answer'


#class Request_recv(models.Model):
    #user_name= models.CharField(max_length=200,default='00000')
    #friend_req= models.CharField(max_length=200,default='00000')