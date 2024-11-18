from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login
from .forms import Register_form,Login_form

def register(request):
    if request.method=='POST':
        form=Register_form(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return HttpResponse(f'<html><h1>Welcome {user} !!!</h1></html>')
        else:
            return HttpResponse('<html><h1>Invalid form </h1></html>')
    else:
        form=Register_form()
    return render(request,'register.html',{'form':form})
        


