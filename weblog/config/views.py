# -*- coding:utf-8 -*-
from django.shortcuts import render

from django.views.generic import ListView

from blog.views import CommonMixin
from .models import Link


class LinkView(CommonMixin, ListView):
    queryset = Link.objects.filter(status=1)
    model = Link
    template_name = 'config/link.html'
    context_object_name = 'links'

