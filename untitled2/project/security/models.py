from datetime import datetime
from django.db import models
#from rwlabel.views import MakeRWLabel,MakeForkLabel
from ifc.rwlabel import RWFM,LabelManager
from rwlabel.views import MakeRWLabel,MakeForkLabel
#from RWFM import MakeRWLabel,MakeForkLabel
import os
from django.contrib.auth.models import User
#from django.contrib.auth import models
# Create your models here.



def doc_rwlabel(self):
    self.object_id = Document_mongo.objects.collection.insert({
			"title": "title",
			"user_id": self.user_name,
			"date_created": datetime.now(),
			"entities": "entities",
			"is_public": False,
		})
    temp = {"_id":str(self.object_id),"is_public":False}
    result = MakeRWLabel(temp,self.request.session)
    print 'label created'+result['bool']
    return
def get_upload_file_name(self,filename):
    doc_rwlabel(self)
    return "uploads/%s/%s" % (self.user_name,filename)



class Document_mongo(models.Model):
    title=models.CharField(max_length=200)
    user_id=models.CharField(max_length=200)
    data_created=models.DateTimeField(auto_now_add=True, blank=True)
    entities=models.CharField(max_length=200)
    is_public = models.BooleanField(default=False)
    class Meta:
        app_label='mongo'

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
    document_name = models.FileField(default='00000')
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
    docfile = models.FileField(default='00000')
    privacy = models.CharField(max_length=2,default='0')
    class Meta:
        db_table = "document_privacy"
#class Request_recv(models.Model):
    #user_name= models.CharField(max_length=200,default='00000')
    #friend_req= models.CharField(max_length=200,default='00000')