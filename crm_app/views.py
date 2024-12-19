from django.shortcuts import render
from .forms import createUserForm
from django.shortcuts import redirect
#for login purpose we need authenticate
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .forms import LoginForm,CreateRecordForm,UpdateRecordForm
from .models import Record
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_protect
#restrictions
from django.contrib.auth.decorators import login_required
def home_view(request):
    return render(request,'index.html')


def register_view(request):
    form=createUserForm()
    if request.method=='POST':
        form=createUserForm(request.POST)
        if form.is_valid():
            #now need to retrive the username,email and two passwords.
            form.save()
            messages.success(request,f'{form.username} account created successfully')
            return redirect('login')
    return render(request,'register.html',{'form':form})

#username.exists()
def login_view(request):
    form=LoginForm()
    if request.method=='POST':
        form=LoginForm(request, data=request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(request,username=username,password=password)

            if user:
                login(request,user)
                messages.success(request,'successfully logged in!!')
                return redirect('dashboard') #need to replace to dashboard page in future.
            # else:
            #     messages.info('Please enter correct credentials')
            #     return redirect('login')
        #if it is model, loginform(instance=model_name)
    return render(request,'login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@csrf_protect
def dashboard_view(request):
    records=Record.objects.all()
    return render(request,'dashboard.html',{'records':records})

@login_required(login_url='login')

def create_record(request):
    form=CreateRecordForm()
    if request.method == 'POST':
        form=CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            # dashboard_view()
            messages.success(request,'Record was created')
            return redirect('dashboard')
    # else:
    messages.warning(request,'Enter records properly')
    return render(request,'create_record.html',{'form':form})
@login_required(login_url='login')
def update_record(request,id):
    #it fetches the data and display it on dashboard page.
    #updating the record based on the id.
    #fetching with the id.
    #<video type='mp4' controls=''>
    record_id=get_object_or_404(Record,id=id)
    # record_id=Record.objects.get(id=id)
    
    if request.method =='POST':
        form=UpdateRecordForm(request.POST,instance=record_id)
        if form.is_valid():

            form.save()
            return redirect('dashboard')
    else:
        form=UpdateRecordForm(instance=record_id)
    return render(request,'update.html',{'form':form})
@login_required(login_url='login')
def single_record(request,id):
    all_records=Record.objects.get(id=id)

    return render(request,'view-record.html',{'all_records':all_records})

def delete_record(request,id):
    record=Record.objects.get(id=id)
    record.delete()
    return redirect('dashboard')