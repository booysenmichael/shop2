from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.core import serializers
from .models import retailers
from .models import items
from django.contrib.auth.models import User

import json

def serialdata(data):
        return serializers.serialize('json',data)

def home(request):
        if not request.user.is_authenticated:
                return render(request,'home/login.html')
        else:
                allItems = items.objects.all()
                profile = User.objects.get(username = request.user)
                return render(request,'items/viewitems.html',{'items':allItems})

def additems(request):
        if not request.user.is_authenticated:
                return render(request,'home/login.html')
        else:
                profile = User.objects.get(username = request.user)
                retailers_data = retailers.objects.filter(disabled=0).order_by('id')
                return render(request, 'items/additems.html',{'retailers':retailers_data})

def addItemsHandler(request):
    if request.method == 'POST':
        newItems = items()
        newItems.item = str(request.POST['item'])
        newItems.qty = request.POST['qty']
        newItems.price = request.POST['price']
        newItems.retailer_id = request.POST['retailer']
        newItems.mustget = request.POST['mustget']
        try:
                newItems.save()
                return HttpResponse('1')
        except:
                return HttpResponse('0')
        
def addItemToListHandler(request):
        if request.method == 'POST':
                theID = request.POST['id']
                theState = request.POST['state']
                if theState == 'Remove':
                        setState = 0
                else:
                        setState = 1

                try:
                        updateItems = items.objects.get(id=theID)
                        updateItems.current = setState       
                        updateItems.save()
                        return HttpResponse('1') #Success
                except:
                        return HttpResponse('0') #Fail

def shoppinglist(request):
        if not request.user.is_authenticated:
                return render(request,'home/login.html')
        else:
                profile = User.objects.get(username = request.user)
                itemsShopping = items.objects.filter(current=1).order_by('id')
                return render(request,'items/startshopping.html',{'items':itemsShopping})


       