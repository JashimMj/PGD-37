from django.shortcuts import render,redirect
from django.contrib import auth,messages
from django.core.files.storage import FileSystemStorage
from .models import *

# Create your views here.

def indexV(request):
    a=UserProfileM.objects.all()
    return render(request,'index.html',{'a':a})

def mainV(request):
    return render(request,'pages/main.html')


def logingV(request):
    if request.method=='POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        user = auth.authenticate(username=name, password=password)
        if user is not None:
            auth.login(request, user)
            if 'next' in request.POST:
                # return redirect(request.POST.get('next'))
                return redirect('/')
            else:
                return redirect('/')
        else:
            messages.info(request, 'User is not valid')
            return redirect('/login/')
    else:
        return render(request,'pages/login.html')

def loguotV(request):
    auth.logout(request)
    return redirect('/login/')

def createuserV(request):
    if request.method == 'POST' and request.FILES:
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        present = request.POST.get('present')
        permanent = request.POST.get('permanent')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User Name already taken')
                return redirect('/Singup/')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'E-Mail already taken')
                return redirect('/Singup/')
            else:
                image = request.FILES['image']
                store = FileSystemStorage()
                filename = store.save(image.name, image)
                profile_pic_url = store.url(filename)
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                sing = UserProfileM(user=user,Phone=phone, Present_Address=present, Permanant_Address=permanent, Image=filename)
                sing.save()
                messages.info(request, 'Data Saved')
                return redirect('/create/user/')
        else:
            messages.info(request, 'password donot match')
            return redirect('/create/user/')
    else:
        return render(request,'admin/usercreate.html')


def DashboardV(request):
    return render(request,'pages/Dashboard.html')
def admindashboardV(request):
    return render(request,'admin/Dashboard.html')

def inventorydashboardV(request):
    return render(request,'inventory/Dashboard.html')
def itemnameV(request):
    return render(request,'inventory/itementry.html')


