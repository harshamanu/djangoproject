from django.shortcuts import redirect, render
from . models import Gallery, Signup
from  . forms import SignupForm,LoginForm,UpdateForm,ChangepasswordForm
from django.contrib import messages
from django.contrib.auth import logout as logouts
# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            place=form.cleaned_data['Place']
            photo=form.cleaned_data['Photo']
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            cpassword=form.cleaned_data['Confirmpassword']
            user=Signup.objects.filter(Email=email).exists()
            if user:
                messages.warning(request,"already exist")
                return redirect('/signup')
            elif password != cpassword:
                messages.warning(request,"incorrect password")
                return redirect('/signup')
            else:
                tab=Signup(Name=name,Age=age,Place=place,Photo=photo,Email=email,Password=password)
                tab.save()
                messages.success(request,"successfull")
                return redirect('/')
    else:
        form=SignupForm()
    return render(request,'signup.html',{'form':form})       

def login(request):
   
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            user=Signup.objects.get(Email=email)
            if not user:
                messages.warning(request,"incorrect")
                return redirect('/login')
            elif password != user.Password:
                messages.warning(request,"incorrect password")
                return redirect('/login')
            else:
               
                messages.success(request,"successfull")
                return redirect('/home/%s' % user.id)
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})        
                
def home(request,id):
    data=Signup.objects.get(id=id) 
    return render(request,'home.html',{'data':data})               
                
def update(request,id):
    user=Signup.objects.get(id=id)
    if request.method=='POST':
        form=UpdateForm(request.POST or None,request.FILES or None,instance=user)
    
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            place=form.cleaned_data['Place']
            photo=form.cleaned_data['Photo']
            email=form.cleaned_data['Email']  
            form.save()
            messages.success(request,"successfull")
            return redirect('/home/%s' % user.id)
    else:
        form=UpdateForm(instance=user)
    return render(request,'update.html',{'form':form})    

def passwordchange(request,id):
    user=Signup.objects.get(id=id)
    if request.method=='POST':
        form=ChangepasswordForm(request.POST)
        if form.is_valid():
            old=form.cleaned_data['Oldpassword']
            new=form.cleaned_data['Newpassword']
            confirm=form.cleaned_data['Confirmpassword']
            if old != user.Password :
                messages.warning(request,"incorrect old password")
                return redirect('/passwordchange/%s' % user.id)
            elif old==new:
                messages.warning(request,"old and new are equal")
                return redirect("/passwordchange/%s" % user.id)
            elif new != confirm:
                messages.warning(request,"incorrect password")
                return redirect('/passwordchange/%s' % user.id)
            else:
                user.Password=new
                user.save()
                messages.success(request,"password changed successfully")
                return redirect('/home/%s' % user.id)
    else:
        form=ChangepasswordForm()
    return render(request,'passwordchange.html',{'form':form,'user':user})            
           
def logout(request):
    logouts(request)
    messages.success(request,"logout successfully")
    return redirect('/')


def gallery(request):
    data=Gallery.objects.all()
    return render(request,'gallery.html',{'data':data})

def details(request,id):
    data=Gallery.objects.get(id=id)
    return render(request,'details.html',{'data':data})                          