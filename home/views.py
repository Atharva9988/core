from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return render(request, "home/index.html")


def livingroom(request):
    print("*" * 10)
    return HttpResponse("<h2> I am the son of home page, I say, 'I am back daddy'</h2>")