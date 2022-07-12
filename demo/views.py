from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm 
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
import time

# Create your views here.
def indexView(request):
    return render(request,'index.html')

@login_required
def dashboardView(request):
    return render(request, 'dashboard.html')

def register(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST) 

        if form.is_valid():
            form.save()
         
            messages.success(request, 'Account created successfully!! Please login to Continue...')
            
            return redirect('login')
        else:
            messages.warning(request, 'Invalid Details! Please try again...')
           



    else:
        form = UserCreationForm(request.POST)
        
 
            
        
    return render(request,'registration/register.html',{'form':form})