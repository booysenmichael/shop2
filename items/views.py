from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.core import serializers
from .models import retailers
from .models import items

import json

def serialdata(data):
        return serializers.serialize('json',data)

def home(request):
        allItems = items.objects.all()
        return render(request,'items/viewitems.html',{'items':allItems})

def additems(request):
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
        itemsShopping = items.objects.filter(current=1).order_by('id')
        return render(request,'items/startshopping.html',{'items':itemsShopping})