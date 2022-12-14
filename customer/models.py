from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class Customer(AbstractBaseUser):
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others'),
    )

    STATUS = (
        ('active', 'Active'),
        ('archived', 'Archived'),
        ('deleted', 'Deleted'),
    )

    first_name = models.CharField(max_length=255, )
    last_name = models.CharField(max_length=255, )
    address = models.TextField()
    is_active = models.BooleanField(default=True, )
    is_staff = models.BooleanField(default=False, )
    is_superuser = models.BooleanField(default=False, )
    gender = models.CharField(max_length=20, choices=GENDER, default='male')
    email = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    status = models.CharField(max_length=20, choices=STATUS, default='active')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'gender', 'address', 'is_superuser', 'is_staff', 'is_active', 'status']
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    class Meta:
        db_table = 'customers'
        verbose_name = 'Customers'
        verbose_name_plural = 'Customers'