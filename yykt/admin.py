# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *
from markdownx.admin import MarkdownxModelAdmin

admin.site.site_header = 'xx课堂'
admin.site.site_title = 'zz系统'
admin.site.index_title = 'yy课堂'
admin.site.site_url = ''

admin.site.disable_action('delete_selected')

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','category','status','price','studyPeople']
    #list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50
    #筛选器
    list_filter =('category', 'status', 'level') #过滤器
    search_fields =('name', 'category') #搜索字段
    date_hierarchy = 'createTime'    #筛选

    #list_editable 设置默认可编辑字段
    #list_editable = ['status', 'price']


class UserAdmin(admin.ModelAdmin):
    list_display = ['phone','nickName','realName','wechatNum','childName','birthday']
    readonly_fields = ('phone','password','nickName','realName','uniqueId','wechatNum','childName','birthday','childSex')

    def has_add_permission(self,request):
        return False

class CollectAdmin(admin.ModelAdmin):
    list_display = ['course','user','createTime','updateTime']
    readonly_fields = ('course','user','createTime','updateTime')

    def has_add_permission(self,request):
        return False

class LikeAdmin(admin.ModelAdmin):
    list_display = ['course','user','createTime','updateTime']
    readonly_fields = ('course','user','createTime','updateTime')

    def has_add_permission(self,request):
        return False

class CommentAdmin(admin.ModelAdmin):
    list_display = ['course','user','comment','level']
    readonly_fields = ('course','user','comment','level')

    def has_add_permission(self,request):
        return False

class BannerAdmin(admin.ModelAdmin):
    pass


admin.site.register(CourseCategoty)
admin.site.register(Tag)
admin.site.register(Course,CourseAdmin)
admin.site.register(Video)
admin.site.register(Audio)
admin.site.register(User,UserAdmin)
admin.site.register(Collect,CollectAdmin)
admin.site.register(Like,LikeAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Banner,BannerAdmin)
admin.site.register(Article,MarkdownxModelAdmin)

