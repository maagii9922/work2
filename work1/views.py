from django.http import HttpResponse
from django.shortcuts import render
from .models import Hereglegch,Baraa

def home(request):
    b=Baraa.objects.all()
    return render(request,'home.html',{'baraa':b})


def login(request):
    # return HttpResponse("ggdfgd")
    return render(request,'login.html')

def insert(request):
    m=request.POST['bner']
    l=request.POST['bprice']
    n=request.POST['btoo']
    k=request.POST['bimage']

    q=Baraa(name=m,price=l,too=n,image=k)
    q.save()

    b=Baraa.objects.all()
    return render(request,'home.html',{'baraa':b})

def zasah(request):
    print(request.GET)
    # print(request.GET['bprice'])
    m=request.GET['bner']
    l=request.GET['bprice']
    n=request.GET['btoo']
    k=request.GET['bimage']
    i=request.GET['bid']
    return render(request,'zasah.html',{'bner':m, 'bprice':l,'btoo':n,'bimage':k,'bid':i})

def zshalgah(request):
    m=request.POST['bner']
    l=request.POST['bprice']
    n=request.POST['btoo']
    k=request.POST['bimage']
    i=request.POST['bid']

    h=Baraa.objects.get(pk=i)

    print(h)
    h.name=m
    h.price=l
    h.too=n
    h.image=k
    h.save()

    b=Baraa.objects.all()
    return render(request,'home.html',{'baraa':b})

def ustgah(request):
    i=request.GET['bid']
    h=Baraa.objects.get(pk=i)
    h.delete()



    b=Baraa.objects.all()
    return render(request,'home.html',{'baraa':b})


def shalgah(request):
    print(request.method)
    x=request.POST['ner']
    y=request.POST['code']

    h=Hereglegch.objects.filter(name=x,code=y)
    # print(h.na//////
    # print(h.code)
    print(len(h))
    if len(h)==1: 
        # return HttpResponse('OK')
        b=Baraa.objects.all()
        return render(request,'home.html',{'user':h[0].name, 'baraa':b})
    elif len(h)==0:
        # return HttpResponse('error')
        return render(request,'login.html',{'aldaa':'aldaa garlaa','buruu':x,'buruu2':y})

        
    return HttpResponse('server error')
