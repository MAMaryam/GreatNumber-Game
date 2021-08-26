from django.shortcuts import render, HttpResponse, redirect
import random 

def index(request):
    if 'randomNumber' not in request.session:
        request.session['randomNumber'] = random.randint(1, 100)
    return render (request, 'index.html')

def inputCalculation (request):
    if int(request.POST['number']) == request.session ['randomNumber']:
        context = {
            "input": "correct!"
        }
    if int(request.POST['number']) < request.session ['randomNumber']:
        context = {
            "input": "too low"
        }

    if int(request.POST['number']) > request.session ['randomNumber']:
        context = {
            "input": "too high"
        }
    return render (request, "index.html", context)

# Create your views here.
