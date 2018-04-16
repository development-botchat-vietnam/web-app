# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from Tkconstants import CASCADE

from django.db import models

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.contrib.auth.models import User
# Create your models here.


# class Account(models.Model):
#     user          = models.OneToOneField(User, on_delete=models.CASCADE)
#     name          = models.CharField(max_length=120, null=True)
#     nickname          = models.CharField(max_length=200, null=True)
#     id_face       = models.CharField(max_length=100, null=True)
#     url_face      = models.CharField(max_length=300, null=True)
#     sex           = models.CharField(max_length=50, null=True)
#     image         = models.CharField(max_length=500, null=True)
#     birtday       = models.DateField()
#     religion      = models.CharField(max_length=200, null=True)
#     location      = models.CharField(max_length=200, null=True)
#     CHOICE_STATUS = (('1', 'Single'),('2', 'Married'),('3', 'Divorce'))
#     status        = models.CharField(choices=CHOICE_STATUS, max_length=1, default= 1)  
#     work          = models.CharField(max_length=200, null=True)
#     likes         = models.CharField(max_length=200, null=True)
#     dislikes      = models.CharField(max_length=200, null=True)
#     hobbies       = models.CharField(max_length=500, null=True)
#     favorite_food = models.CharField(max_length=200, null=True)
#     favorite_drink= models.CharField(max_length=200, null=True)
#     motto_in_life = models.CharField(max_length=500, null=True)
#     CHOICE_TYPE   = (('1', 'Admin'),('2', 'Manager'),('3', 'Author'),('4', 'Member'))
#     type_account  = models.CharField(choices=CHOICE_TYPE, max_length=1, default= 4)
#     date_register = models.DateTimeField(auto_now_add=True)
#     CHOICE_ACTION = (('1', 'True'),('0', 'False'))
#     active        = models.CharField(choices=CHOICE_ACTION, max_length=1, default=0)
#     def __str__(self):
#         return self.name

class Catalog(models.Model):
    name            = models.CharField(max_length=100)
    unsigned_name   = models.CharField(max_length=200)
    order_sort      = models.IntegerField()
    CHOICE_PUBLIC   = (('1', 'True'), ('0', 'False'))
    public          = models.CharField(default=0, max_length=1, choices=CHOICE_PUBLIC)
    meta_desc       = models.CharField(max_length=120)
    meta_key        = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name            = models.CharField(max_length=200)
    unsigned_name   = models.CharField(max_length=200)
    created         = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Posts(models.Model):
    title               = models.CharField(max_length=200)
    unsigned_title      = models.CharField(max_length=250)
    excerpt             = models.TextField()
    image               = models.ImageField(upload_to='posts/')
    date                = models.DateTimeField(auto_now_add=True)
    author                = models.OneToOneField(User, on_delete=models.CASCADE)
    content             = models.TextField()
    id_catalog          = models.ForeignKey(Catalog, on_delete=models.CASCADE, verbose_name='Catalog')
    view                = models.IntegerField(default=0, verbose_name ='View')
    tag                 = models.ManyToManyField(Tag, related_name='posts')
    CHOICE_HIGHLIGHT    = (('1', 'True'), ('0', 'False'))
    highlight           = models.CharField(default=0, max_length=1, choices=CHOICE_HIGHLIGHT)
    CHOICE_PUBLIC       = (('1', 'Public'), ('0', 'Private'))
    public              = models.CharField(default=1, max_length=1, choices=CHOICE_PUBLIC)
    show_group          = models.IntegerField(default=0)
    def __str__(self):
        return self.title


class Comment(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    content         = models.TextField()
    date            = models.DateTimeField(auto_now_add=True)
    id_post         = models.ForeignKey(Posts, on_delete=models.CASCADE, verbose_name='Post')
    CHOICE_PUBLIC   = (('1','True'),('0', 'False'))
    public          = models.FileField(default=1, choices=CHOICE_PUBLIC, max_length=1)

    def __str__(self):
        return self.content


class Setup(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    about = models.CharField(max_length=250)
    image = models.ImageField(upload_to='avatar/')

class Online(models.Model):
    ip = models.GenericIPAddressField()
    created = models.DateTimeField(auto_now_add=True)
