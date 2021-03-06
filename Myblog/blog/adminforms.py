# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from dal import autocomplete
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Category, Tag


class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label="摘要", required=False)
    content = forms.CharField(
        widget=CKEditorUploadingWidget(), label="内容"
    )
    # category = forms.ModelChoiceField(
    #     queryset=Category.objects.all(),
    #     widget=autocomplete.ModelSelect2(url='category-autocomplete'),
    #     label='分类',
    # )
    # tag = forms.ModelMultipleChoiceField(
    #     queryset=Tag.objects.all(),
    #     widget=autocomplete.ModelSelect2Multiple(url='tag-autocomplete'),
    #     label='标签',
    # )
