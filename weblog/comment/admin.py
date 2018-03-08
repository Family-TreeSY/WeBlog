# -*- coding:utf-8 -*-


from django.contrib import admin
from django.utils.html import format_html

from .models import Comment
from django.urls import reverse
from weblog.custom_site import custom_site
from .adminforms import CommentAdminForm
# from typeidea.custom_admin import BaseOwnerAdmin


@admin.register(Comment, site=custom_site)
class CommentAdmin(admin.ModelAdmin):
# class CommentAdmin(BaseOwnerAdmin):
    form = CommentAdminForm
    list_display = ['target', 'nickname', 'email', 'website', 'created_time','operator']
    # list_display_links = ['post', 'nickname', 'email']
    list_filter = ['nickname']
    search_fields = ['email', 'nickename']
    actions_on_top = True
    date_hierarchy = 'created_time'

    '''
    编辑页面
    '''
    # fieldsets = (
    #     ('基础设置', {
    #         'fields': (('nickname', 'post'),
    #                    'website',
    #                    'content',
    #                    'email',),
    #     }),
    #     ('高级设置', {
    #         'classes': ('collapse', 'addon'),
    #         'fields': ('website',)
    #     })
    # )
    fields = (('nickname', 'post'),
              'website',
              'email',
              'content')

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:comment_comment_change', args=(obj.id,))
        )

    operator.short_description = '操作'