from django.shortcuts import render, redirect
from.models import Receipe
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.


def receipes(request):
    if request.method == "POST":
        
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        
        Receipe.objects.create(
            receipe_description=receipe_description,
            receipe_name=receipe_name,
            receipe_image=receipe_image,
            )
        return redirect('/receipes/')
    queryset = Receipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))
    context = {'receipe':queryset}
    return render(request, 'receipes.html', {'receipes':queryset})


def update_receipe(request, id):
    queryset = Receipe.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description

        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect('/receipes/')


    context = {'receipe':queryset}
    return render(request, 'update_receipe.html', context)  


def delete_receipe(request, id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipes/')


def login_page(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password'),
        )
        if user is None:
            messages.error(request, "Invalid username or password")
            return redirect('/login/')
        login(request, user)
        return redirect('/receipes/')
    return render(request, 'login.html')