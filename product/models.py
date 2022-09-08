from django.db import models
from django_mysql.models import ListTextField


class Product(models.Model):

    name   = models.CharField(max_length=255, )
    image_url = models.JSONField(blank=True , null=True)
    stock  = models.IntegerField()
    price  = models.IntegerField()

    status = models.CharField(default = 'active', max_length = 25)
    created_at = models.DateField(auto_now_add = True)
    updated_at  = models.DateField(auto_now = True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'

