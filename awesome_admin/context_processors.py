# -*- coding: utf-8 -*-

from django.conf import settings

def awesome_ui(request):
    return {
        'AWESOME_UI': settings.AWESOME_UI,
    }

