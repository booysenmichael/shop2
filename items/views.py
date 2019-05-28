from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.core import serializers
from .models import retailers
from .models import items
from django.core import serializers
import json
from django.contrib.auth.models import User
from .models import shopList
from .models import shopListDetails
from decimal import Decimal
import decimal




def serialdata(data):
        return serializers.serialize('json',data)

def getShopListDetails(data):
        list = [] #create list
        for theItem in data:
                list.append({'id':theItem.id,'name':theItem.item.item_description,'qty':theItem.qty,'price':str(theItem.price),'retailer':theItem.item.retailer.retailer_description})
        return list

def home(request):
        if not request.user.is_authenticated:
                return render(request,'home/login.html')
        else:
                allItems = items.objects.all()
                shoppingListName = shopList.objects.filter(completed=0)
                profile = User.objects.get(username = request.user)
                return render(request,'items/viewitems.html',{'items':allItems,'shoppingListName':shoppingListName})

def additems(request):
        if not request.user.is_authenticated:
                return render(request,'home/login.html')
        else:
                profile = User.objects.get(username = request.user)
                retailers_data = retailers.objects.filter(disabled=0).order_by('id')
                return render(request, 'items/additems.html',{'retailers':retailers_data})

def addItemsHandler(request):
    if request.method == 'POST':
        current_user = request.user
        newItems = items()
        newItems.item_description = str(request.POST['item'])
        newItems.qty = request.POST['qty']
        newItems.price = request.POST['price']
        newItems.retailer_id = request.POST['retailer']
        newItems.mustget = True
        newItems.addedBy = User.objects.get(pk=request.user.id)

        try:
                newItems.save()
                return HttpResponse('1')
        except Exception as e:
                return HttpResponse(e)
        
def addItemToListHandler(request):
        if request.method == 'POST':
                theState = request.POST['state']
                shoppingList = shopListDetails()
                if theState != 'Remove':
                        theID = items.objects.get(pk=request.POST['id'])
                        theList = shopList.objects.get(pk=request.POST['list']) 
                        theQty = request.POST['qty']
                        thePrice = request.POST['price']
                        shoppingList.item=theID
                        shoppingList.shop_list=theList
                        shoppingList.price = thePrice
                        shoppingList.qty = theQty
                        try:
                                shoppingList.save()
                                return HttpResponse('1') #Success
                        except Exception as e:
                                return HttpResponse(e) #Fail
                else:
                        theID = request.POST['id']
                        theList = shopList.objects.get(pk=request.POST['list'])
                        theItem = shopListDetails.objects.filter(item_id=theID,shop_list_id=theList)
                        
                        try:
                                theItem.delete()
                                return HttpResponse('1') #Success
                        except Exception as e:
                                return HttpResponse(e) #Fail
                        


        #if request.method == 'POST':
        #        theID = request.POST['id']
        #        theState = request.POST['state']
        #        if theState == 'Remove':
        #                setState = 0
        #        else:
        #                setState = 1
        #
        #        try:
        #                updateItems = items.objects.get(id=theID)
        #                updateItems.current = setState       
        #                updateItems.save()
        #                return HttpResponse('1') #Success
        #        except:
        #                return HttpResponse('0') #Fail

def shoppinglist(request):
        if not request.user.is_authenticated:
                return render(request,'home/login.html')
        else:
                profile = User.objects.get(username = request.user)
                shoppingListName = shopList.objects.filter(completed=0)
                return render(request,'items/startshopping.html',{'shoppingListName':shoppingListName})

def addListHandler(request):
        if request.method == 'POST':
                newList = shopList()
                newList.list_name = request.POST['listname']
                newList.completed = 0
                newList.total = 0.00
                try:
                        newList.save()
                        return HttpResponse(newList.id)
                except Exception as e:
                        return JsonResponse(serialdata(e),safe=False)

def getItemList(request):
        if request.method == 'POST':
                listID = request.POST['listId']
                theShopList = shopListDetails.objects.all()
                theShopListNew = shopListDetails.objects.all()
                returndata = getShopListDetails(theShopList)
                return HttpResponse(json.dumps(returndata), content_type="application/json")

def deleteItem(request):
        if request.method == 'POST':
                tID = request.POST['tID']
                theShopList = shopListDetails.objects.get(pk=tID)
                theShopList.delete()
                theShopListNew = shopListDetails.objects.all()
                returndata = getShopListDetails(theShopListNew)
                return HttpResponse(json.dumps(returndata), content_type="application/json")

def getAllItems(request):
        if request.method =='POST':
                allItems = items.objects.all()
                list = []
                for item in allItems:
                        list.append({'id':item.id,'name':item.item_description,'retailer':item.retailer.retailer_description,'mustget':item.mustget,'price':str(item.price),'qty':str(item.qty)})
                return HttpResponse(json.dumps(list), content_type="application/json")