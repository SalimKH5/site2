from django.shortcuts import render

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Files

# Imaginary function to handle an uploaded file.


def home(request):
    return render(request,"kinship/home.html")

def verification(request):
    context={'file':Files.objects.all()}
    return render(request,"kinship/verification.html",context)

def contact(request):
    return HttpResponse("Contact us")


