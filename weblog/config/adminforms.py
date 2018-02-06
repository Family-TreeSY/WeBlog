# -*- coding:utf-8 -*-

from  django import forms


class SideBarAdminForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea, label='内容', required=False)
