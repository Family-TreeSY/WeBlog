# -*- coding:utf-8 -*-
import markdown

from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    '''
    CharField(): 字符型字段
     blank=True: 表示Form填写该字段的时候可以为空值
    TextField()：正文内容会很长不能用max_length来限制
    help_text: 提示
    BooleanField: 布尔值，判断是否
    ForeignKey(): 多对一，一个用户可以创建多个分类，添加外键
    DateTimeField(): 时间字段
    auto_now_add=True：当记录创建时赋予值
    '''
    STATUS_ITEMS = (
        (1, '正常'),
        (2, '删除'),
    )
    name = models.CharField(max_length=128, verbose_name='名字')
    status = models.PositiveIntegerField(
        default=1, choices=STATUS_ITEMS, verbose_name='状态')
    is_nav = models.BooleanField(default=False, verbose_name='是否为导航')
    user = models.ForeignKey(User, verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '分类'

    def __str__(self):
        return self.name


class Tag(models.Model):
    STATUS_ITEMS = (
        (1, '正常'),
        (2, '删除'),
    )
    name = models.CharField(max_length=128, verbose_name='名字')
    status = models.PositiveIntegerField(
        default=1, choices=STATUS_ITEMS, verbose_name='状态')
    user = models.ForeignKey(User, verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '标签'

    def __str__(self):
        return self.name


class Post(models.Model):
    '''
    blank=True: 表示Form填写该字段的时候可以为空值
    TextField()：正文内容会很长不能用max_length来限制
    help_text: 提示
    many_to_many()：多对多，一个标签可以有多篇文章，多篇文章同样可以拥有多个标签
    '''
    STATUS_ITEMS = (
        (1, '上线'),
        (2, '删除'),
    )
    title = models.CharField(max_length=128, verbose_name='标题')
    desc = models.CharField(max_length=1024, blank=True, verbose_name='摘要')
    content = models.TextField(verbose_name='正文', help_text='正文必须是MarkDown')
    is_markdown = models.BooleanField(verbose_name='使用markdown', default=True)
    status = models.PositiveIntegerField(
        default=1, choices=STATUS_ITEMS, verbose_name='状态')
    category = models.ForeignKey(Category, verbose_name='分类')
    tag = models.ManyToManyField(Tag, related_name="posts", verbose_name='标签')
    user = models.ForeignKey(User, verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    last_update_time = models.DateTimeField(
        auto_now=True, verbose_name='最后修改时间')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.is_markdown:
            self.content = markdown.markdown(self.content, extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ])
        return super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = verbose_name_plural = '文章'
        ordering = ['-id']
