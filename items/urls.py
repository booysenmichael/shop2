from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name='items_home'),
    path('add',views.additems,name='items_add'),
    path('addItemsHandler',views.addItemsHandler),
    path('addItemToListHandler', views.addItemToListHandler),
    path('shoppinglist',views.shoppinglist,name='shoppinglist'),
    path('addListHandler',views.addListHandler),
    path('getItemList',views.getItemList),
    path('deleteItem',views.deleteItem),
    path('getAllItems',views.getAllItems),
]