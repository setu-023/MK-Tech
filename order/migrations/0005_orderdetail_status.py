# Generated by Django 3.2 on 2022-09-08 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='status',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]