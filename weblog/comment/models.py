# -*- coding:utf-8 -*-

from django.db import models


class Comment(models.Model):
    STATUS_ITMES = (
        (1, '正常'),
        (2, '删除'),
    )
    target = models.CharField(max_length=200, null=True, verbose_name='文章')
    nickname = models.CharField(max_length=180, verbose_name='名字')
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITMES, verbose_name='状态')
    email = models.EmailField(verbose_name='邮箱')
    website = models.URLField(verbose_name='网站')
    content = models.CharField(max_length=255, verbose_name='内容')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    # def __str__(self):
    #     return self.nickname


    class Meta:
        verbose_name = verbose_name_plural = '评论'
        ordering = ['-id']