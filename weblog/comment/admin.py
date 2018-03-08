# -*- coding:utf-8 -*-


from django.contrib import admin
from django.utils.html import format_html

from .models import Comment
from django.urls import reverse
from weblog.custom_site import custom_site
from .adminforms import CommentAdminForm


@admin.register(Comment, site=custom_site)
class CommentAdmin(admin.ModelAdmin):
    form = CommentAdminForm
    list_display = ['target', 'nickname', 'email', 'website', 'content', 'created_time', 'operator']
    # list_filter = ['nickname']
    # search_fields = ['email', 'nickename']
    actions_on_top = True
    date_hierarchy = 'created_time'

    # '''
    # 编辑页面
    # '''
    #

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:comment_comment_change', args=(obj.id,))
        )

    operator.short_description = '操作'