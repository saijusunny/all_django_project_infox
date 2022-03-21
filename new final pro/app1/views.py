
import os
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout # visable pages using django login session method
from  django.contrib.auth.decorators import login_required
from .models import userlogin
from .models import title
from .models import curt

#-------------------admin section-----------------------------------------------------
@login_required(login_url='adminlogin')
def addproduct_page(request):
    return render(request,'add_product.html')

#product add section
@login_required(login_url='adminlogin')
def upload_product(request):
    return render(request,'upload section.html')

# add products
@login_required(login_url='adminlogin')
def add_product(request):
    if request.method == 'POST':
        titles = request.POST['title']
        image = request.FILES.get('image')
        price = request.POST['price']
        uid= User.objects.get(id=request.user.id)
        print(uid)
        t = title(title=titles,itmes=image, price=price, user=uid)
        t.save()
        print("save")
        return redirect('pro_home')

#to display our product
@login_required(login_url='adminlogin')
def ourpro(request):
    ttl=title.objects.filter(user=request.user.id)
    context = {
        'titles':ttl
    }
    return render(request,'our_products.html',context)
# display uploaded items in upload page
@login_required(login_url='adminlogin')
def pro_home(request):
    titles=title.objects.filter(user=request.user.id)
    context = {
        'titles':titles
    }
    return render(request,'upload section.html',context)
    
#-------------------------------------------------------------------------------------


#curt Section
@login_required(login_url='adminlogin')
def cart(request,pk):
    crt=title.objects.get(id=pk)
    return render(request, 'curt.html',{'crt':crt})

@login_required(login_url='adminlogin')
def add_curt(request):
    if request.method == "POST":
        titles = request.POST['title']
        if request.FILES.get('file') is not None:
            image=request.FILES['file']
        else:
            image = "static/image/default.jpg"
        price = request.POST['price']
        uid= User.objects.get(id=request.user.id)
        t = curt(
        title = titles,
        itmes = image,
        price = price,
        user=uid,
        )
        t.save()
        print("save")
        return redirect('curt_view')

#curt View
@login_required(login_url='adminlogin')
def curt_view(request):
    ct=curt.objects.filter(user=request.user.id)
    return render(request, 'curt_view.html', {'ct':ct})

@login_required(login_url='adminlogin')
def delete_cart(request,pk):
    products=curt.objects.get(id=pk)

    products.delete()
    return redirect('curt_view')


#PRODUCT VIEW FOR USERS---------------------------------------------------------------
@login_required(login_url='adminlogin')
def shop(request,pk):
    
    title1=title.objects.get(id=pk)
    context = {
        'title1':title1
    }
    return render(request,'shop.html',context)

@login_required(login_url='adminlogin')
def shop2(request,pk):
  clm=curt.objects.get(id=pk)
  return render(request, 'shop2.html', {'clm':clm})

#------------------------------------------------------------

#profile section
@login_required(login_url='adminlogin')
def profile(request):
    result=userlogin.objects.filter(user=request.user.id).last()
    return render(request,'profile.html', {'result':result})

    
#home For user after login
@login_required(login_url='adminlogin')
def home(request):
    prod=title.objects.all()
    context = {
        'titles':prod
    }
    return render(request,'home.html',context)

 #home For user befor login   

def index(request):


    return render(request, 'index.html')



def signup(request):
    return render(request, 'signup.html')

def loginpage(request):
    return render(request, 'login.html')

#this function is login visable pages using login session method
@login_required(login_url='adminlogin')
def about(request):
    return render(request, 'about.html')



#Complete profile
@login_required(login_url='adminlogin')
def complete_pro(request):
    return render(request,'complete profile.html')

#compltet profile section
@login_required(login_url='adminlogin')
def signup_details(request):
    if request.method == "POST":
        nm=request.POST['name']
        uname=request.POST['username']
        upass=request.POST['password']
        repas=request.POST['repassword']
        if request.FILES.get('file') is not None:
            image=request.FILES['file']
        else:
            image = "static/image/icon.png"
        eum=request.POST['email']
        uid= User.objects.get(id=request.user.id)
        print(uid)

        result=userlogin(
            name=nm,
            username=uname,
            password=upass,
            repassword=repas,
            image=image,
            email=eum,
            user=uid,
                            
            )
        result.save()
        return redirect('profile')

#editpage
@login_required(login_url='adminlogin')
def edit(request,pk):
    products=userlogin.objects.get(id=pk)
    return render(request,'profileedit.html', {'products':products})


#profile edit Section
@login_required(login_url='adminlogin')
def edit_details(request,pk):
    if request.method=='POST':
        products = userlogin.objects.get(id=pk)
        products.name=request.POST.get('name')
        products.username=request.POST.get('username')
        products.password=request.POST.get('password')
        products.repassword=request.POST.get('repassword')
        products.email=request.POST.get('email')
        # if len(products.image)>0:
        #     os.remove(products.image.path)
        if request.FILES.get('file') is not None:
            print('hai')
            if not products.image =="static/image/icon.png":
                os.remove(products.image.path)
                products.image = request.FILES['file']
            else:
                products.image = request.FILES['file']
        else:
            os.remove(products.image.path)
            products.image ="static/image/icon.png"
        
        products.save()
        return redirect('profile')
    return render(request, 'profileedit.html')

#profile delete section
@login_required(login_url='adminlogin')
def delete_product(request,pk):
    products=userlogin.objects.get(id=pk)
    if not products.image =="static/image/icon.png":
                os.remove(products.image.path)
    else:
        pass
    products.delete()
    return redirect('index')
    
@login_required(login_url='adminlogin')
def delete_items(request,pk):
    products=title.objects.get(id=pk)
    products.delete()
    return redirect('ourpro')
    
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
        return redirect('adminlogin')
    else:
        return render(request, 'signup.html')

#login page
def adminlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        # request.session['uid'] = user.id #visable pages using session method
        if user is not None:
            # login(request, user) #this function is login visable pages using django login session method
            auth.login(request, user)
            messages.info(request, f'Welcome {username}')#pass users name to welcome page
            return redirect('about')
        else:
            messages.info(request, 'invalid username and password, try again')
            return redirect('loginpage')
    else:
        return redirect('loginpage')



# logoutpage
@login_required(login_url='adminlogin') #login  session method
def adminlogout(request):
    # if request.user.is_authenticated: # visable pages using django login session method
    #request.session['uid']= '' #visable pages using session method
    auth.logout(request)
    return redirect('index')
