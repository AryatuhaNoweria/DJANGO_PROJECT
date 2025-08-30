from django.shortcuts import render

# Create your views here.
def indexpage(request):
    #logic here
    return render(request, "index.html")

def aboutpage(request):
    #logic here
    return render(request, "about.html")

def projectspage(request):
    #logic here
    return render(request, "projects.html")