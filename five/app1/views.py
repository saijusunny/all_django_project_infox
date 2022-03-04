
from django.shortcuts import render, redirect
from django.conf import settings
from django.shortcuts import render, redirect
from app1.form import studentforms
from django.core.mail import send_mail



# Create your views here.
def index(request):
    return render(request,'index.html')

def admin_login(request):
    if request.method == "POST":
        username=request.POST.get('uname')
        password=request.POST.get('upass')
        print(username, password)
        if username == 'saiju':
            if password == '421765':
                return redirect('stdform')
        

        #return render(request,'form.html')
# def admin_login(request):
#     username='saiju'
#     password='421765'
#     if request.uname == username: #input field Name for username
#         if request.upass == password: #input field Name for password
#             return redirect('form')
#     return render(request, 'form.html')


def stdform(request):
    form=studentforms()
    if request.method == 'POST': 
        form=studentforms(request.POST) #save table data to form from form.py
        if form.is_valid():  #used to mverify entered value is valid
            form.save()
            subject='Registration Successfully' #subject
            message='Dear Candidate,\n Your registration is successfully completed' #messege
            recipient=form.cleaned_data.get('email')
            send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            return redirect('/')
    return render(request, 'form.html', {'form':form})