from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as loginuser

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


def home(request):
    
    return render(request,'index.html')




def login(request):
    
    if request.method == "GET":
        form = AuthenticationForm()
        context = { "form" : form }
        
        return render(request, 'login.html', context=context)
    
    else:
        form = AuthenticationForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('passowrd')
            user = authenticate(username = username, password = password)
            print("Authenticated::", user)  
            if user is not None:
                loginuser(request, user)
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
        
        