# -*- coding:utf-8 -*-

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Link, SideBar
from weblog.custom_site import custom_site
from .adminforms import SideBarAdminForm


@admin.register(Link, site=custom_site)
class LinkAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'user', 'href', 'status', 'weight', 'created_time', 'operator'
    ]
    actions_on_top = True
    date_hierarchy = 'created_time'

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:config_link_change', args=(obj.id,))
        )

    operator.short_description = '操作'

@admin.register(SideBar, site=custom_site)
class SideBarAdmin(admin.ModelAdmin):
    form = SideBarAdminForm
    list_display = [
        'title', 'user', 'content', 'status', 'display_type', 'created_time', 'operator'
    ]
    actions_on_top = True
    date_hierarchy = 'created_time'


    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:config_sidebar_change', args=(obj.id,))
        )
    operator.short_description = '操作'
