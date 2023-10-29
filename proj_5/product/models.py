from django.db import models

# Create your models here.
class product_model(models.Model):
    # pid = models.AutoField()
    name = models.CharField(max_length=50)
    desc = models.TextField(max_length=200)
    price = models.PositiveIntegerField()
    discount = models.PositiveSmallIntegerField()
    date = models.DateTimeField(auto_now=True)