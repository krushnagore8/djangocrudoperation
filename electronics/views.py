from django.shortcuts import render
from .models import Product
from .forms import ProductForm
# Create your views here.
def home(request):
    prod=Product.objects.all()
    form=ProductForm()
    return render(request,'electronics/home.html',{"prod":prod, "form":form})


def update_data(request,id):
    if request.method=="POST":
        pi=Product.objects.get(pk=id)
        fm=ProductForm(request.POST,isinstance=pi)
        if fm.is_valid():
            fm.save()
        else:
            pi=Product.objects.get(pk=id)
            fm=ProductForm(instance=pi)
        return render(request,'electronics/update.html',{'form':fm})