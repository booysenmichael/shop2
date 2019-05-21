from django.db import models

class items(models.Model):
    item = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    qty = models.IntegerField(default=0)
    current = models.IntegerField(default=0)
    retailer = models.ForeignKey(to='retailers', null=True,on_delete=models.CASCADE)
    mustget = models.BooleanField(default=False)

class retailers(models.Model):
    retailer = models.CharField(max_length=255)
    disabled = models.BooleanField(default=False)


