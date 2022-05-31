from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from .models import user,post
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
isLogged=False
uName=""

def login(request):
    global isLogged
    if isLogged:
        return redirect("/feed")
    if request.method =="POST":
        value=request.POST["password"]
        value2=request.POST["username"]
        
        if user.objects.filter(userName=value2).exists():
            if user.objects.filter(userName=value2,password=value).exists():
                isLogged=True
                global uName
                uName=value2
                return redirect("/feed")
        return HttpResponse("sifre yada username yanlıs")

    return render(request,"login.html")      


def signUp(request):
    if request.method == "POST":
        value=user(userName = request.POST["username"],name = request.POST["ad"],lastName = request.POST["soyAd"],password= request.POST["password"])
        value2=request.POST["username"]
        if user.objects.filter(userName=value2).exists():
            
            return redirect("/signUp2")
        value.save()    
        return redirect("/login")

        
    return render(request,"signUp.html")
def signUp2(request):


        
    return render(request,"signUp2.html")    

def feed(request):
    post1= post.objects.all()
    
    name=uName
    
    context= {'feed': post1,
    'a': name
    }
    global isLogged
    if not isLogged:
        return redirect("/login")
    if request.method =="POST":    
        

        value=post(title = request.POST["text"], userId=uName)   
        value.save()

    return render(request,"feed.html",context) 
    
def myP(request):
    global uName
    post1= post.objects.all().filter(userId=uName)
    
    
    context= {'feed': post1}
    global isLogged
    if not isLogged:
        return redirect("/login")
    

    
    return render(request,"myP.html",context)
def logout(request):
    global uName
    global isLogged
    uName=""
    isLogged=False
    return redirect("/login")