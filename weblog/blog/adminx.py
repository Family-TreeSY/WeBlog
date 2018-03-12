# -*- coding:utf-8 -*-
import xadmin
from xadmin.layout import Fieldset, Row
# from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Post, Category, Tag
# from weblog.custom_site import custom_site
from .adminforms import PostAdminForm
from weblog.adminx import BaseOwnerAdmin


# @admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    '''
    list_display: 展示页面要展示的功能
    search_fields: 搜索栏
    actions_on_top: 动作栏
    fields: 编辑页面要展示的功能
    '''
    form = PostAdminForm
    list_display = [
        'title', 'user', 'status', 'category', 'pv', 'uv', 'created_time', 'operator'

    ]
    search_fields = ['title']
    list_filter = ('user',)
    actions_on_top = True
    date_hierarchy = 'created_time'

    # fields = (
    #     ('title', 'user'),
    #     'status',
    #     'category',
    #     'tag',
    #     'desc',
    #     ('content', 'is_markdown')
    # )
    form_layout = (
        Fieldset(
            "基础信息",
            'title',
            'desc',
            Row('category', 'tag', 'status'),
            'is_markdown',
            'content',
        ),
    )
    exclude = (
        'user',
        'pv',
        'uv',
    )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )
    # 添加描述，这句代码不加，管理界面会显示operator
    operator.short_description = '操作'
xadmin.site.register(Post, PostAdmin)

# @admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = [
        'name', 'status', 'is_nav', 'created_time'
    ]
    fields = (
        'name',
        'status',
        'is_nav'
    )
xadmin.site.register(Category, CategoryAdmin)

# @admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = [
        'name', 'status', 'created_time',
    ]
    fields = (
        'name',
        'status',
    )
xadmin.site.register(Tag, TagAdmin)