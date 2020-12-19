from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def upload_page(request):
    return render(request,"upload.html")

def local_page(request):
    return render(request,"local.html")

def drive_page(request):
    return render(request,"drive.html")
