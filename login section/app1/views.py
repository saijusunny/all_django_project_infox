
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def loginpage(request):
    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')


#signup page
def usercreate(request):
    if request.method=="POST":
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        cpass=request.POST['cpassword']
        email=request.POST['email']

        if password==cpass:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This Username Is Already Exists!!!!!')
                return redirect('signup')
            else:
                user=User.objects.create_user(
                    first_name=fname,
                    last_name=lname,
                    username=username,
                    password=password,
                    email=email,
                )
                user.save()
        else:
            messages.info(request, 'Password doesnot match!!!!!')
            return redirect('signup')
        return redirect('login')
    else:
        return render(request, 'signup.html')

#login page
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            messages.info(request, f'Welcome {username}')#pass users name to welcome page
            return redirect('about')
        else:
            messages.info(request, 'invalid username and password, try again')
            return redirect('loginpage')
    else:
        return redirect('loginpage')

# logoutpage
def logout(request):
    auth.logout(request)
    return redirect('index')

