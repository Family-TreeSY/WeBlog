# -*- coding: utf-8 -*-

from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = 'WeBlog管理'
    site_title = 'WeBlog'
    index_title = '首页'

custom_site = CustomSite(name='cus_admin')