# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-08 00:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='名字')),
                ('href', models.URLField(verbose_name='链接')),
                ('status', models.PositiveIntegerField(choices=[(1, '上线'), (2, '删除')], default=1, verbose_name='状态')),
                ('weight', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1, help_text='权重越高越靠前', verbose_name='权重')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '友链',
                'verbose_name_plural': '友链',
            },
        ),
        migrations.CreateModel(
            name='SideBar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='名字')),
                ('content', models.CharField(max_length=255, verbose_name='内容')),
                ('display_type', models.PositiveIntegerField(choices=[(1, 'HTML'), (2, '最新文章'), (3, '最热文章'), (4, '最新评论')], default=1, verbose_name='展示状态')),
                ('status', models.PositiveIntegerField(choices=[(1, '上线'), (2, '删除')], default=1, verbose_name='状态')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '侧边栏',
                'verbose_name_plural': '侧边栏',
            },
        ),
    ]
