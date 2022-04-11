from django.shortcuts import render , HttpResponse
from django.shortcuts import render,HttpResponse,redirect
from home.models import Feedback
from django.contrib import messages
import joblib
# Create your views here.

def home(request):
    lr = joblib.load('aqi_model.sav')

    l = []
    if request.method=="POST":
        l.append(request.POST['pm2.5'])
        l.append(request.POST['pm10'])
        l.append(request.POST['no2'])
        l.append(request.POST['co2'])
        l.append(request.POST['so2'])

        ans = lr.predict([l])

        return render(request,"home.html", {'ans':ans})

    return render(request,"home.html")
    

def feed(request):
    if request.method =="POST":
        name=request.POST['name']
        exp=request.POST['exp']
        any=request.POST['any']
        rate=request.POST['rate']
        feedback=Feedback(name=name, exp=exp, any=any, rate=rate)
        feedback.save()
    return render(request, "feedback.html")