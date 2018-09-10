#!/usr/bin/env python
# encoding: utf-8
'''
@author: Ricardo
@license: (C) Copyright 2018-2019 @yang.com Corporation Limited.
@contact: 659706575@qq.com
@software: made@Yang
@file: urls.py
@time: 2018/9/7 0007 12:43
@desc:
'''
from django.urls import path, include
from . import views
# APP下的urls  管理路径，从setting中的url分离过来，
urlpatterns=[
    path('page/',include([
        path('login/', views.login, name='login'),
        path('login_logic/', views.login_logic, name='login_logic'),
        path('regist/', views.regist, name='regist'),
        path('regist_logic', views.regist_logic, name='regist_logic'),
        path('introduce/',views.introduce,name='intro'),
        path('menu/',views.menu,name='menu'),
    ])),
    path('ajax/',views.ajax,name='ajax')


]