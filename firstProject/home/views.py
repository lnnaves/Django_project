from django.shortcuts import render
# Create your views here.

def home(request):
    print('Home Django')
    return render(request,'home/index.html')
