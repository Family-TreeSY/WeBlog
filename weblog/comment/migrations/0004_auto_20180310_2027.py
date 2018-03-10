# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-10 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_auto_20180310_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=255, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='nickname',
            field=models.CharField(max_length=180, verbose_name='名字'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.PositiveIntegerField(choices=[(1, '正常'), (2, '删除')], default=1, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='target',
            field=models.CharField(max_length=200, null=True, verbose_name='文章'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='website',
            field=models.URLField(verbose_name='网站'),
        ),
    ]