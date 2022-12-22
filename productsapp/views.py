from django.shortcuts import render, redirect
from .models import Products
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

def index(request):
    return render(request, "index.html", {"products": Products.objects.all()})
    
def addproduct(request):
    if request.method == "POST":
        name = request.POST.get("name", False)
        price = request.POST.get("price", False)
        image = request.FILES.get("img", False)
        discrip = request.POST.get("discrip", False)
        if image and name:
            p = Products.objects.create(name = name, price=price, image=image, discription=discrip)
            p.save()
            messages.success(request, "Product added: "+name)
        else:
            messages.error(request, "You must add image and name for product")
    return render(request, 'add_product.html')

def details(request, pk):
    return render(request, "details.html", {"product": Products.objects.get(id=pk)})

@staff_member_required
def update(request, pk):
    if request.method == "POST":
        name = request.POST['name']
        price = request.POST['price']
        image = request.FILES['img']
        discrip = request.POST['discrip']
        p = Products.objects.get(id = pk)
        p.name = name
        p.price = price
        p.image = image
        p.discription = discrip
        p.save()
        return redirect("/")
    return render(request, "update.html", {"product":Products.objects.get(id=pk)})

@staff_member_required
def delete(request, pk):
    p = Products.objects.get(id = pk)
    p.delete()
    return redirect("/")