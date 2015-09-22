from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.files import File
from project.settings import MEDIA_ROOT
from .models import Document,Request_send,Shared,Friends
from .forms import SignUpForm,ContactForm,DocumentForm,RequestSendForm,FriendForm,SharedForm,SaveForm
from django.db import connection

# Create your views here.
def home(request):
    find_friend=[]
    cursor=connection.cursor()
    form1=SaveForm(request.POST or None)
    if request.method=="POST":
        form = DocumentForm(request.POST,request.FILES)
        var=request.POST.get("SearchBox","")
        print var
        if(var):
            sql ='Select distinct user_name from documents where user_name ="%s"' %(var)
            cursor.execute(sql)
            q= cursor.fetchall()
            for f in q:
                find_friend.append(f[0])
    else:
        form = DocumentForm()
    documents = Document.objects.all()


    friend_list=[]
    #form = FriendForm(request.POST or None)
    sql ='Select * from security_request_send where friend_req= "%s" and user_name !="%s"' %(request.user.username,request.user.username)
    cursor.execute(sql)
    all_users= cursor.fetchall()
    for usr in all_users:
        friend_list.append(usr[1])
    q= Friends.objects.filter(user_name=request.user.username)
    # print q
    return render_to_response(
            'home.html',
            {'friends': q,'document': documents,'find_friend':find_friend,'txt':form1,'form':form,'friend_list':friend_list},
            context_instance=RequestContext(request)
        )       
    
def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        email= form.cleaned_data.get("email")
        print email
        
    context = {
    "form" : form
    }
        
    return render(request,"contact.html",context)

#def upload_file(request):
    #if request.method == 'POST':
        #form = UploadFileForm(request.POST, request.FILES)
        #if form.is_valid():
            #handle_uploaded_file(request.FILES['file'])
            #return HttpResponseRedirect('project.view.list')
    #else:
        #form = UploadFileForm()
    #return render_to_response('list.html', {'form': form})
def list(request):
    # Handle file upload
    form1=SaveForm(request.POST or None)
    if request.method == 'POST':
        #print request.FILES['file'].filename
        form = DocumentForm(request.POST,request.FILES)
        print "checking form validation"
        if form1.is_valid():
            message= form1.cleaned_data.get("message")
            print message
        if form.is_valid():
            #newdoc = Document(docfile = request.FILES['docfile'])
            #handle_upload_file(request.FILES['file'])
            instance=form.save(commit=False)
            
            instance.user_name= request.user
            instance.read = True
            instance.write = True
            instance.owner = True
            instance.save()
            # Redirect to the document list after POST
            return HttpResponseRedirect('/')
    else:
        print "in form_valid"
        form = DocumentForm() # A empty, unbound form
    #print "in form_invalid"
    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'document': documents,'form':form,'txt':form1},
        context_instance=RequestContext(request)
    )
def find_friend(request):
    
    if request.method == 'POST':
        form = RequestSendForm(request.POST)
        print "checking form validation"
        if form.is_valid():
            instance=form.save(commit=False)
            print "in form_valid"
            instance.user_name= request.user.username
            instance.friend_req = request.POST.get("frnd_name","")        
            print 'instance.frnd_req '+instance.friend_req
            instance.save()        
            return HttpResponseRedirect('/')
        else:
            print "invalid_form" 
    sql ='Select * from auth_user where username NOT IN'\
    '(Select friend_req from security_request_send where user_name= "%s")'%(request.user.username) 
    all_users= User.objects.raw(sql)
    #all_users=all_users.exclude(username=request.user)
    return render_to_response(
        'find_friend.html',
        {'users': all_users},
        context_instance=RequestContext(request)
    )
def registration_complete(request):
    return render(request,'registration/registration_complete.html',{})
def friend(request):
    form = FriendForm(request.POST or None)
    q= Friends.objects.filter(user_name=request.user.username)
    return render_to_response(
        'friend.html',
        {'friends': q},
        context_instance=RequestContext(request)
    )    
    

def notification(request):
    if request.method == 'POST':
        form= FriendForm(request.POST)
        print "checking form validation"
        if form.is_valid():
            instance=form.save(commit=False)
            print "in form_valid(notification)"
            instance.user_name= request.user.username
            instance.friend_name = request.POST.get("frnd_name","")        
            print 'instance.frnd_req '+instance.friend_name
            instance.save() 
            e=Request_send.objects.filter(user_name=instance.friend_name,friend_req=request.user.username)
            e.delete();
            return HttpResponseRedirect('/')
        else:
            print "invalid_form"    
    sql ='Select * from security_request_send where friend_req= "%s" and user_name !="%s"' %(request.user.username,request.user.username)
    print sql
    all_users= Request_send.objects.raw(sql)
        #all_users=all_users.exclude(username=request.user)
    return render_to_response(
            'notification.html',
            {'users': all_users},
            context_instance=RequestContext(request)
        )    

def shared(request):
    if request.method == 'POST':
        form= DocumentForm(request.POST or None)
        print "checking form validation"
        if form.is_valid():
            instance=form.save(commit=False)
            print "in form_valid"
            instance.user_name= request.POST.get("friend_select","")
            instance.docfile = request.POST.get("docfile","")
            instance.friend_name = request.POST.get("frnd_name","") 
            instance.write = ((request.POST.get("write_select","")) in ("True","1"))
            #print "instance.write: "+ instance.write
            instance.grantor = request.user.username
            #print 'instance.frnd_req '+instance.friend_name
            instance.save()        
            return HttpResponseRedirect('/')
        else:
            print "invalid_form"       
    
    #print "in form_invalid"
    # Load documents for the list page
    sql = "Select * from security_friends where user_name='%s'"%(request.user.username)
    #print sql
    friend = Friends.objects.raw(sql)
    sql = "Select * from documents where user_name='%s'"%(request.user.username)
    #print sql    
    shared = Document.objects.raw(sql)
    
        # Render list page with the documents and the form
    return render_to_response(
            'shared.html',
            {'shared': shared,'friends':friend,},
            context_instance=RequestContext(request)
        )    


def save(request):
    form1 = SaveForm(request.POST or None)
    print "inside save form"
    if form1.is_valid():
        file_text= form1.cleaned_data.get("message")
        file_name = form1.cleaned_data.get("filePath")
        with open(MEDIA_ROOT+'/'+file_name,'w') as f:
            myfile= File(f)
            myfile.write(file_text)
        
        
        print file_text,file_name
        
    context = {
    "txt" : form1
    }
        
    return render_to_response(
    'save.html',
    {'txt': form1},
    context_instance=RequestContext(request)
) 


def demo(request):
    var=request.POST.get("SearchBox","")
    friend=''
    print var
    if(var):
        sql ='Select * from documents where user_name ="%s"' %(var)
        print sql
        friend= Document.objects.raw(sql)     
        
        
    return render_to_response(
        'demo.html',
        {'find_friend':friend},
        context_instance=RequestContext(request)
    )     