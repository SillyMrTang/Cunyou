# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     adminx
   Description :
   Author :       Administrator
   date：          2019/3/29 0029
-------------------------------------------------
   Change Activity:
                   2019/3/29 0029:
-------------------------------------------------
"""
from xadmin import views
from .models import TypeModel, TypeContent
import xadmin


class TypeAdmin(object):
    list_display = ['id', 'name', 'image', 'create_time']
    search_fields = ['name', ]
    ordering = ('id',)


class ContentAdmin(object):
    list_display = ['id', 'name', 'image', 'path', 'type']
    search_fields = ['name', ]
    ordering = ('id',)


class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True  # 支持切换主题


class GlobalSettings(object):
    site_title = "村游六品后台管理"


xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(TypeModel, TypeAdmin)
xadmin.site.register(TypeContent, ContentAdmin)
