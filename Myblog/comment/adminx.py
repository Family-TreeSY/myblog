# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.html import format_html
from django.urls import reverse

import xadmin
from xadmin.layout import Fieldset, Row

from .models import Comment
from Myblog.adminx import BaseOwnerAdmin


# @admin.register(Comment, site=custom_site)
class CommentAdmin(BaseOwnerAdmin):
    list_display = [
        "target",
        "nickname",
        "status",
        "email",
        "website",
        "created_time",
        "operator",
    ]

    fields = (
        ("target", "status"),
        "content",
        "website",
        "email",
    )

    form_layout = (
        Fieldset(
            Row('target', 'status'),
            'content',
            'website',
            'email',
        ),
    )

    exclude = (
        'author',
    )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse("cus_admin:comment_comment_change", args=(obj.id,))
        )
    # 不加简短描述，管理界面会显示operator
    operator.short_description = "操作"


xadmin.site.register(Comment, CommentAdmin)
