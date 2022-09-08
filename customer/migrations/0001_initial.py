# Generated by Django 3.2 on 2022-09-07 14:08

import customer.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], default='male', max_length=20)),
                ('email', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=150)),
                ('status', models.CharField(choices=[('active', 'Active'), ('archived', 'Archived'), ('deleted', 'Deleted')], default='active', max_length=20)),
            ],
            options={
                'verbose_name': 'Customers',
                'verbose_name_plural': 'Customers',
                'db_table': 'customers',
            },
            managers=[
                ('objects', customer.models.CustomUserManager()),
            ],
        ),
    ]
