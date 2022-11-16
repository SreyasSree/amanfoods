from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import LoginForm , RegistrationForm
from django.contrib.auth import login , authenticate , logout
from django.contrib import messages



# Create your views here.

def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            password = cd['password']
            user = authenticate(request,username=username,password=password)
            # print(user)
            if user is not None:
                login(request,user)
                return redirect('home:index')
            else:
                print('invalid credentials!')

        


    form = LoginForm()
    return render(request , 'accounts/login.html', {'form':form})

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            
            messages.success(request,'you have signed up successfully!')
            return redirect('home:index')
            # return HttpResponse('Your account has been created successfully!')

        else:
            # messages.error(request,'passwords does not match')
            return render(request,'accounts/signup.html', {'form':form})
    form = RegistrationForm()
    return render(request , 'accounts/signup.html', {'form':form})


def signout(request):
    logout(request)
    return redirect('home:index')