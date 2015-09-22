from django import forms

from .models import SignUp,Document,Friends,Request_send,Friends,Shared


class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']

#class UploadFileForm(forms.Form):
        #title = forms.CharField(max_length=50)
        #file = forms.FileField()

class DocumentForm(forms.ModelForm):
    #title = forms.CharField(max_length=50)
    #print title
    #docfile = forms.FileField()
    print "In document form"
    class Meta:
        model=Document
        fields = ['docfile']
class FriendForm(forms.ModelForm):
    class Meta:
        model= Friends
        exclude = ['user_name','friend_name']
class RequestSendForm(forms.ModelForm):
    class Meta:
        model=Request_send
        exclude= ['user_name','friend_req']

class SharedForm(forms.ModelForm):
    class Meta:
        model = Document
        exclude= ['user_name','docfile','read','write','owner']


class SaveForm(forms.Form):
    filePath = forms.CharField(widget = forms.HiddenInput(),max_length=100,required=False)
    message= forms.CharField(widget=forms.Textarea,label='',required=False)
    
    
#class RequestRecvForm(forms.ModelForm):
    #class Meta:
        #model=Request_recv
        #exclude= ['user_name','friend_req']