# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Comment, Tag, Catalog, Posts, Setup


class CatalogAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'order_sort', 'public')


class CommentAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('id', 'date')
    raw_id_fields = ('id_post',)

# class AccountAdmin(admin.ModelAdmin):
#     search_fields = ['name', 'username']
#     list_display = ('name', 'nickname', 'sex', 'active')
#     fields = ('name', 'birtday', 'religion', 'location', 'status', 'work', 'likes', 'dislikes', 'hobbies', 'favorite_food', 'favorite_drink', 'motto_in_life', 'type_account')

class TagAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'created')

class PostsAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    ordering = ('-title',)
    search_fields = ['title', 'author', 'public']
    list_display = ('title', 'date', 'view', 'author', 'id', 'public')
    fields = ('title','unsigned_title','excerpt', 'image', 'author', 'content', 'id_catalog', 'tag', 'highlight', 'public')
    filter_horizontal = ('tag',)
    raw_id_fields = ('author', 'id_catalog',)


admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Posts, PostsAdmin)
admin.site.register(Setup)
#admin.site.register(Account, AccountAdmin)