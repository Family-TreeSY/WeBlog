# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-10 12:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_auto_20180310_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='link',
            name='href',
            field=models.URLField(verbose_name='链接'),
        ),
        migrations.AlterField(
            model_name='link',
            name='status',
            field=models.PositiveIntegerField(choices=[(1, '上线'), (2, '删除')], default=1, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='link',
            name='title',
            field=models.CharField(max_length=255, verbose_name='名字'),
        ),
        migrations.AlterField(
            model_name='link',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='link',
            name='weight',
            field=models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1, help_text='权重越高越靠前', verbose_name='权重'),
        ),
        migrations.AlterField(
            model_name='sidebar',
            name='content',
            field=models.CharField(max_length=255, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='sidebar',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='sidebar',
            name='display_type',
            field=models.PositiveIntegerField(choices=[(1, 'HTML'), (2, '最新文章'), (3, '最热文章'), (4, '最新评论')], default=1, verbose_name='展示状态'),
        ),
        migrations.AlterField(
            model_name='sidebar',
            name='status',
            field=models.PositiveIntegerField(choices=[(1, '上线'), (2, '删除')], default=1, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='sidebar',
            name='title',
            field=models.CharField(max_length=255, verbose_name='名字'),
        ),
        migrations.AlterField(
            model_name='sidebar',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
    ]
