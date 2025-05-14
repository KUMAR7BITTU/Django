from django.http import HttpResponse
from django.shortcuts import render

# kisi request pe hum home return karenge.
def home(request):
    #return HttpResponse("Hello, world . you are at chai aur coffee home page.")
    return render(request,'website/index.html')

# index.html is stored inside templates folder, this already defined internally in the settings .So, we don't need to specify templates here.

def about(request):
    #return HttpResponse("Hello, world . you are at chai aur coffee about page.")
    return render(request,'website/about.html')

def contact(request):
    return HttpResponse("Hello, world. you are at chai aur coffee contact page. ")