from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'map/index.html')

def Carson(request):
    return render(request, 'extensions/Carson.html')

def Fort_Yates(request):
    return render(request, 'extensions/Fort_Yates.html')

def Linton(request):
    return render(request, 'extensions/Linton.html')