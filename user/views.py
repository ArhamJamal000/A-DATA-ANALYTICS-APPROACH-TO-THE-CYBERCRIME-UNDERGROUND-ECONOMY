from urllib import request

from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from user.forms import UserForm, UploadForm, FeedbackForm
from user.models import RegisterModel, UploadModel, ChatModel, RequestModel


def index(request):
    if request.method == "POST":
        usid = request.POST.get('userid')
        pswd = request.POST.get('password')
        try:
            enter = RegisterModel.objects.get(userid=usid,password=pswd)
            request.session['userid']=enter.id
            return redirect('uploadfile')
        except:
            pass
    return render(request,'user/index.html')

def register(request):
    if request.method == "POST":
        forms = UserForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('index')
    else:
        forms = UserForm()

    return render(request,'user/register.html',{'form':forms})
def feedback(request):
    if request.method == "POST":
        forms = FeedbackForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('feedback')
    else:
        forms = FeedbackForm()
    return render(request,'user/homepage.html',{'form':forms})
def uploadfile(request):

    if request.method == "POST":
        forms = UploadForm(request.POST or None,request.FILES)
        if forms.is_valid():
            tt=forms.save(commit=False)
            uid=request.session['userid']
            enter = RegisterModel.objects.get(id=uid)
            tt.userDet=enter
            tt.save()
            return redirect('uploadfile')
    else:
         forms= UploadForm()
    return render(request,'user/uploadfile.html',{'form':forms})

def mydetails(request):
    userid = request.session['userid']
    ted = RegisterModel.objects.get(id=userid)
    return render(request,'user/mydetails.html',{'object':ted})
def updatedetails(request):
    userid = request.session['userid']
    objec = RegisterModel.objects.get(id=userid)
    if request.method == "POST":
        FirstName = request.POST.get('FirstName', '')
        LastName = request.POST.get('LastName', '')
        DateOfBirth = request.POST.get('DateOfBirth', '')
        Age = request.POST.get('Age', '')
        UserId = request.POST.get('UserId', '')
        Password = request.POST.get('Password', '')
        MobileNumber = request.POST.get('MobileNumber', '')
        EmailId = request.POST.get('EmailId', '')
        Gender = request.POST.get('Gender', '')

        obj = get_object_or_404(RegisterModel,id=userid)
        obj.firstname = FirstName
        obj.lastname = LastName
        obj.dob = DateOfBirth
        obj.age = Age
        obj.userid = UserId
        obj.password = Password
        obj.mobilenumber = MobileNumber
        obj.emailid = EmailId
        obj.gender = Gender

        obj.save(update_fields=["firstname", "lastname", "dob", "age", "userid", "password", "mobilenumber", "emailid","gender", ])
        return redirect('mydetails')

    return render(request,'user/updatedetails.html',{'obj': objec})

def viewdocument(request):
    obj=UploadModel.objects.filter(request="accpted")
    return render(request,'user/viewdocument.html',{'list_object':obj,})
def logout(request):
    return render(request,'logout')

def request(request,pk):
    userid = request.session['userid']
    uobj = RegisterModel.objects.get(id=userid)
    obj = UploadModel.objects.get(id=pk)
    RequestModel.objects.create(accessone=uobj,accesstwo=obj)
    return redirect('viewdocument')
def download(request):
    userid = request.session['userid']
    uobj = RegisterModel.objects.get(id=userid)
    obj =RequestModel.objects.filter(accessone=uobj)
    return render(request,'user/downloadpage.html',{'object':obj})