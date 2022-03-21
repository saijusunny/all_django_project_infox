#from multiprocessing import context
import os
from unicodedata import category
#from turtle import title
#from unicodedata import category
#from unittest import skipIf
from django.shortcuts import render,redirect

from userApp.models import UserProfile,Category,Images,title,product,multimage

# Create your views here.

#..************Default Image Edit and Delete**************
def home(request):
    return render(request,'home.html')
    
def load_profile_page(request):
    return render(request,'profile.html')

def add_profile(request):
    if request.method == 'POST':
        uname=request.POST['name']
        uemail=request.POST['email']
        uaddress=request.POST['address']
        #image=request.FILES.get('file')
        if request.FILES.get('file') is not None:
            image = request.FILES['file']
        else:
            image = "/static/image/default.png"
        userPrfl = UserProfile(name=uname,email=uemail,addrress=uaddress,image=image)
        print("save")
        userPrfl.save()
        return redirect('show_details')
    return render(request,'profile.html')

def show_details(request):
    user_data = UserProfile.objects.all()
    return render(request,'show_profile.html',{'user_data':user_data})

def edit_user_page(request,pk):
    udata=UserProfile.objects.get(id=pk)
    return render(request,'edit_profile.html',{'udata':udata})

def edit_user_data(request,pk):
    if request.method=='POST':
        userdatas = UserProfile.objects.get(id=pk)
        userdatas.name = request.POST.get('name')
        userdatas.email = request.POST.get('email')
        userdatas.addrress = request.POST.get('address')
        if request.FILES.get('file') is not None:
            if not userdatas.image == "/static/image/default.png":
                os.remove(userdatas.image.path)
                userdatas.image = request.FILES['file']
            else:
                userdatas.image = request.FILES['file']
        else:
            os.remove(userdatas.image.path)
            userdatas.image = "/static/image/default.png" 
        userdatas.save()
        return redirect('show_details')
    return render(request, 'edit_profile.html')


def delete_user_data(request,pk):
    udatas=UserProfile.objects.get(id=pk)
    if udatas.image is not None:
        if not udatas.image == "/static/image/default.png":
            os.remove(udatas.image.path)
        else:
            pass
    udatas.delete()
    return redirect('show_details')

#...*****Add Multiple Images.....

def pro_home(request):
    titles=title.objects.all()
    context = {
        'titles':titles
    }
    return render(request,'products/index.html',context)

def addproduct_page(request):
    return render(request,'products/add_product.html')

def add_product(request):
    if request.method == 'POST':
        titles = request.POST['title']
        image = request.FILES.get('image')
        t = title(title=titles,itmes=image)
        t.save()
        print("save")
        return redirect('pro_home')

#def addimage_page(request):
 #   titles=title.objects.all()
  #  return render(request,'products/add_image.html',{'titles':titles})

def add_image(request,pk):
    if request.method == 'POST':
        images = request.FILES.getlist('images')
        titls = title.objects.get(id=pk)
        for img in images:
            prdcts= product(title=titls,image=img)
            prdcts.save()
            print("save")
        return redirect('pro_home')
    return render(request,'products/add_image.html')


def product_details(request,pk):
    title1=title.objects.get(id=pk)
    context = {
        'title1':title1
    }
    return render(request,'products/product_deatils.html',context)

#...........***GALLERY***...............

def addimage(request):
    catgrs = Category.objects.all()
    context={
        'catgrs':catgrs,
    }
    return render(request,'gallery/add.html',context)

def add(request):
    if request.method == 'POST':
        catgors = request.POST.get('category')
        cts = Category.objects.get(id=catgors)
        img = request.FILES.get('image')
        desc = request.POST.get('des')
        imags = Images(category=cts,image=img,description=desc)
        imags.save()
        print("save")
        return redirect('gallery')
    return render(request,'gallery/add.html')

def gallery(request):
    ctgs = request.GET.get('category')
    imgs = Images.objects.all()
    if ctgs is not None:
        imgs = Images.objects.filter(category__category_name=ctgs)
    catgrs = Category.objects.all()
    
    context = {
        'catgrs':catgrs,
        'imgs':imgs,
        }
    return render(request,'gallery/gallery.html',context)

def showimage(request,pk):
    img = Images.objects.get(id=pk)
    mulimgs = multimage.objects.filter(category_id=img.category_id)
    linkimg = multimage.objects.get(id=pk)
    context={
        'img':img,
        'mulimgs':mulimgs,
        'linkimg':linkimg,
    }
    return render(request,'gallery/image.html',context)