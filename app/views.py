from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as loginUser, logout
from app.forms import Youdo_Medo_Form
from app.models import Youdo_Medo
from django.contrib.auth.decorators import login_required

# Create your views here.

"""
def home(request):
    
    # print("Hello World!...This is Home")
    
    html = '''
    
        <h1>Home Page</h1>
        
        <ul>
            <li>Item 1</li>
            <li>Item 2</li>
            <li>Item 3</li>
            <li>Item 4</li>
        </ul>
        
        <p> This is Para</p>
        
        <button>Login</button>
        
        <a href='https://www.facebook.com/syed.noveedh'>Go to facebook</a>
        '''
    
    
    # return HttpResponse("Response from View File")
    return HttpResponse(html)

"""

@login_required(login_url='login')   # if user is not logged in it wont go to home page and redirects to login page
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = Youdo_Medo_Form
        youdos = Youdo_Medo.objects.filter(user = user).order_by('priority')
        return render(request,'index.html', {'form':form, 'youdos' : youdos})




def login(request):
    
    if request.method == "GET":
        form = AuthenticationForm()
        context = { "form" : form }
        
        return render(request, 'login.html', context=context)
    
    else:
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            print("Authenicated:", user)
            if user is not None:
                loginUser(request, user)
                return redirect('home')
                 
        else:
            context = { "form" : form }
        
            return render(request, 'login.html', context=context)
        
            


def signUp(request):
    
    if request.method == 'GET':
    
        form = UserCreationForm()
        context = {
            "form" : form
        }
        return render(request, 'signup.html', context=context)
    
    else:
        
        print(request.POST)
        form = UserCreationForm(request.POST)
        context = {
            "form" : form
        }
        
        
        if form.is_valid():
            user = form.save()
            print(user)
            # return HttpResponse("Form is Valid")
            if user is not None:
                return redirect('login')
        else:
            # return HttpResponse("Form is Valid")
            return render(request, 'signup.html', context=context)
        


@login_required(login_url='login')
def add_youdo(request):
    
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = Youdo_Medo_Form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            youdo = form.save(commit=False)
            youdo.user = user
            youdo.save()
            print(youdo)
            
            return redirect('home')
        else:
            return render(request, 'index.html', conext={'form' : form})
        
        
        
        
def signout(request):
    logout(request)
    return redirect('login')



@login_required(login_url='login')
def delete_youdo(request, id):
    print(id)
    Youdo_Medo.objects.get(pk = id).delete()
    return redirect('home')
    
    
    
@login_required(login_url='login')
def change_status(request, id, status):
    youdo = Youdo_Medo.objects.get(pk = id)
    youdo.status = status
    youdo.save()
    return redirect('home')