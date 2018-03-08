# -*- coding:utf-8 -*-

from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 10:
            raise forms.ValidationError('亲！写长点！')
        return content

    class Meta:
        model = Comment
        fields = [
            'nickname', 'email', 'website', 'content'
        ]


