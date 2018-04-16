# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question2(models.Model):
    id_question = models.AutoField(primary_key=True)
    question = models.TextField(blank=True, null=True)
    a = models.CharField(max_length=1000, blank=True, null=True)
    b = models.CharField(max_length=1000, blank=True, null=True)
    c = models.CharField(max_length=1000, blank=True, null=True)
    d = models.CharField(max_length=1000, blank=True, null=True)
    CHOICE_ANSWER   = (('A', 'a'), ('B', 'b'), ('C', 'c'), ('D', 'd'))
    anwser = models.CharField(max_length=100, choices=CHOICE_ANSWER, null=True)
    active = models.IntegerField( null=True, default=1)
    created = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'question_2'

class ChooseAnswer(models.Model):
    id_choose = models.AutoField(primary_key=True)
    id_face = models.CharField(max_length=100, blank=True, null=True)
    anwser = models.CharField(max_length=100, blank=True, null=True)
    question = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'choose_answer'
