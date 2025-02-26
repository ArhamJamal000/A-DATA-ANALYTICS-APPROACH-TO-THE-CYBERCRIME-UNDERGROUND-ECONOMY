from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from user.models import RegisterModel, UploadModel, RequestModel, ChatModel, FeedbackModel


def login(request):
    if request.method == "POST":
        if request.method == "POST":
            usid = request.POST.get('userid')
            pswd = request.POST.get('password')
            if usid == 'admin' and pswd == 'admin':
                return redirect('viewuploadfile')

    return render(request,'fileadmin/login.html')
def viewpage(request):
    obj = RegisterModel.objects.all()
    return render(request,'fileadmin/viewpage.html',{'object':obj})
def viewuploadfile(request):
    obj = UploadModel.objects.all()
    return render(request,'fileadmin/viewuploadfile.html',{'object':obj})

def accept(request,pk):
    obj=UploadModel.objects.get(id=pk)
    obj.request = "accpted"
    obj.save(update_fields=["request"])
    return redirect('viewuploadfile')

def reject(request,pk):
    obj=UploadModel.objects.get(id=pk)
    obj.request = "rejected"
    obj.save(update_fields=["request"])
    return redirect('viewuploadfile')

def deleteobj(request,pk):
    obj= get_object_or_404(UploadModel,pk=pk)
    obj.delete()
    return redirect('viewuploadfile')
def viewuserrequest(request,):
    userid = request.session['userid']
    userobj = RegisterModel.objects.get(id=userid)
    object=RequestModel.objects.all()
    obj=ChatModel.objects.filter(Q(userId=userobj))
    return render(request,'fileadmin/viewuserrequest.html',{'view_list':object})
def accepts(request,pk):
    obj=RequestModel.objects.get(id=pk)
    obj.request = "accpted"
    obj.save(update_fields=["request"])
    return redirect('viewuserrequest')

def rejects(request,pk):
    obj=RequestModel.objects.get(id=pk)
    obj.request = "rejected"
    obj.save(update_fields=["request"])
    return redirect('viewuserrequest')

def deleteobjs(request,pk):
    obj= get_object_or_404(RequestModel,pk=pk)
    obj.delete()
    return redirect('viewuserrequest')

def viewchat(request,pk):
    reqw=RequestModel.objects.get(id=pk)
    user_one_obj=reqw.accessone
    user_two_obj=reqw.accesstwo.userDet

    #userObj = RegisterModel.objects.get(id=userid)
    #pko=RegisterModel.objects.get(pk=pk)
    object=ChatModel.objects.filter(Q(userId=user_one_obj,senderId=user_two_obj.id)| Q(userId=user_two_obj,senderId=user_one_obj.id))
    val = 0

    for o in object:
        word = o.chat
        result = word.find('underworld market',)
        vara = word.find('illegal sales')
        varb = word.find('illicit business')
        varc = word.find('shady dealings')
        vard = word.find('underground market')
        vare = word.find('gray market')
        varf = word.find('underground')

        if result != -1:
            val = val + 1
        if vara !=-1:
            val = val + 1
        if varb !=-1:
            val = val + 1
        if varc !=-1:
            val = val + 1
        if vard !=-1:
            val = val + 1
        if vare !=-1:
            val = val + 1
        if varf !=-1:
            val = val + 1

    if val > 5:
        res = 'NEGATIVE'
    else:
       res = 'POSITIVE'

    return render(request,'fileadmin/viewchat.html',{'view_list':object,'result':res,})

def viewfeedbackpage(request):
    obj=FeedbackModel.objects.all()
    return render(request,'fileadmin/viewfeedbackpage.html',{'object':obj})

def chartpage(request,chart_type):
    w1,w2,w3,w4,w5,w6,w7=0,0,0,0,0,0,0
    object = ChatModel.objects.all()
    val=0
    for o in object:
        word = o.chat
        result = word.find('underworld market', )
        vara = word.find('illegal sales')
        varb = word.find('illicit business')
        varc = word.find('shady dealings')
        vard = word.find('underground market')
        vare = word.find('gray market')
        varf = word.find('underground')

        if result !=-1:
            w1 = w1 + 1
        if vara != -1:
            w2 = w2 + 1
        if varb != -1:
            w3 = w3 + 1
        if varc != -1:
            w4 = w4 + 1
        if vard != -1:
            w5 = w5 + 1
        if vare != -1:
            w6 = w6 + 1
        if varf != -1:
            w7 = w7 + 1

    return render(request,'fileadmin/chartpage.html',{'chart_type':chart_type,'v1':w1,'v2':w2,'v3':w3,'v4':w4,'v5':w5,'v6':w6,'v7':w7})
def logout(request):
    return render(request,'logout')
