from django.shortcuts import render

# Create your views here
def store(request):
        return render(request,'online/store.html')

def cart(request):
    return render(request,'online/cart.html')

def checkout(request):
    return render(request,'online/checkout.html')
