# -*- coding:utf-8 -*-
from django.shortcuts import render

from django.views.generic import ListView

from blog.views import CommonMixin
from .models import Link
# from comment.forms import CommentForm
from comment.views import CommentShowMixin

class LinkView(CommonMixin, CommentShowMixin, ListView):
    queryset = Link.objects.filter(status=1)
    model = Link
    template_name = 'config/link.html'
    context_object_name = 'links'

    # def get_context_data(self, **kwargs):
    #     kwargs.update({
    #         'comment_form': CommentForm(),  # initial: 指定表单的初始数据
    #     })
    #     return super(LinkView, self).get_context_data(**kwargs)