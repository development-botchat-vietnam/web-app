# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CheckLove(models.Model):
    id_love = models.AutoField(primary_key=True)
    id_face_author = models.CharField(max_length=100, blank=True, null=True)
    id_face_react = models.CharField(max_length=100, blank=True, null=True)
    text_write = models.CharField(max_length=1000, blank=True, null=True)
    insert_data = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'check_love'

    def __str__(self):
        return self.id_face_author

class JoinGame(models.Model):
    id_join = models.AutoField(primary_key=True)
    id_face = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'join_game'

    def __str__(self):
        return self.id_face


class Question(models.Model):
    id_question = models.AutoField(primary_key=True)
    question = models.TextField(blank=True, null=True)
    anwser = models.CharField(max_length=100, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    cancel = models.IntegerField(blank=True, null=True)
    winner = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question'

    def __str__(self):
        return self.question


class RankLastMonth(models.Model):
    id_rank = models.AutoField(primary_key=True)
    id_face = models.CharField(max_length=100, blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rank_last_month'
    
    def __str__(self):
        return self.id_face


class Score(models.Model):
    id_score = models.AutoField(primary_key=True)
    id_face = models.CharField(max_length=100, blank=True, null=True)
    text_write = models.CharField(max_length=1000, blank=True, null=True)
    score = models.IntegerField()
    type_score = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'score'
    
    def __str__(self):
        return self.id_face


class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    id_face = models.CharField(unique=True, max_length=100, blank=True, null=True)
    name_user = models.CharField(max_length=200, blank=True, null=True)
    image_user = models.CharField(max_length=300, blank=True, null=True)
    sex = models.CharField(max_length=100, blank=True, null=True)
    url_user = models.CharField(max_length=300, blank=True, null=True)
    check_exists = models.IntegerField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    religion = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    work = models.CharField(max_length=200, blank=True, null=True)
    likes = models.CharField(max_length=200, blank=True, null=True)
    dislikes = models.CharField(max_length=200, blank=True, null=True)
    hobbies = models.CharField(max_length=200, blank=True, null=True)
    favorite_food = models.CharField(max_length=200, blank=True, null=True)
    favorite_drink = models.CharField(max_length=200, blank=True, null=True)
    motto_in_life = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
    
    def __str__(self):
        return self.name_user