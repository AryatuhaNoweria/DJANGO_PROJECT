from django.shortcuts import render

# Create your views here.
def calcpage(request):
    return render(request,'calc.html')