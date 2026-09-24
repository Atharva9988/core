from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):

    players = [
        {'name' : 'Abhishek Sharma', 'age' : 23, 'totalruns': 1630},
        {'name' : 'Shubhman Gill', 'age' : 25, 'totalruns': 7291},
        {'name' : 'Virat Kohli', 'age' : 37, 'totalruns': 28359},
        {'name' : 'Rohit Sharma', 'age' : 39, 'totalruns': 20427}, 
    ]

    for player in players:
        print(player)

    return render(request, "home/index.html" , context={'players': players})


def livingroom(request):
    print("*" * 10)
    return HttpResponse("<h2> I am the son of home page, I say, 'I am back daddy'</h2>")