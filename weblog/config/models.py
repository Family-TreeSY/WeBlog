# -*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User



class Link(models.Model):
    STATUS_ITEM = (
        (1, '上线'),
        (2, '删除'),
    )
    title = models.CharField(max_length=255, verbose_name='名字')
    href = models.URLField(verbose_name='链接')
    user = models.ForeignKey(User, verbose_name='作者')
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEM, verbose_name='状态')
    weight = models.PositiveIntegerField(default=1, choices=zip(range(1, 6), range(1, 6)), verbose_name='权重', help_text='权重越高越靠前')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = '友链'


class SideBar(models.Model):
    STATUS_ITEM = (
        (1, '上线'),
        (2, '删除'),
    )
    STATUS_TYPE = (
        (1, 'HTML'),
        (2, '最新文章'),
        (3, '最热文章'),
        (4, '最新评论')
    )
    title = models.CharField(max_length=255, verbose_name='名字')
    user = models.ForeignKey(User, verbose_name='作者')
    content = models.CharField(max_length=255, verbose_name='内容')
    display_type = models.PositiveIntegerField(default=1, choices=STATUS_TYPE, verbose_name='展示状态')
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEM, verbose_name='状态')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = '侧边栏'