from django.db import models
from django.contrib.auth.models import User

class retailers(models.Model):
    retailer_description = models.CharField(max_length=255)
    disabled = models.BooleanField(default=False)

class items(models.Model):
    item_description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    qty = models.IntegerField(default=0)
    current = models.IntegerField(default=0)
    retailer = models.ForeignKey(to='retailers', null=True,on_delete=models.CASCADE)
    mustget = models.BooleanField(default=False)
    addedBy = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.item
  
    
class shopList(models.Model):
    list_name = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    date_added = models.DateField(auto_now_add=True)
    date_completed = models.DateField(auto_now=True)
    total = models.DecimalField(max_digits=10,decimal_places=2)

class shopListDetails(models.Model):
    item = models.ForeignKey(items,null=True,on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    shop_list = models.ForeignKey(to='shopList',null=True,on_delete=models.CASCADE)
    