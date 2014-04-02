# Copyright (c) 2014 AnsibleWorks, Inc.
# All Rights Reserved.

# Django REST Framework
from rest_framework import renderers

class BrowsableAPIRenderer(renderers.BrowsableAPIRenderer):
    '''
    Customizations to the default browsable API renderer.
    '''

    def get_rendered_html_form(self, view, method, request):
        '''Never show auto-generated form (only raw form).'''
        obj = getattr(view, 'object', None)
        if not self.show_form_for_method(view, method, request, obj):
             return
        if method in ('DELETE', 'OPTIONS'):
             return True  # Don't actually need to return a form

class PlainTextRenderer(renderers.BaseRenderer):

    media_type = 'text/plain'
    format = 'txt'

    def render(self, data, media_type=None, renderer_context=None):
        if not isinstance(data, basestring):
            data = unicode(data)
        return data.encode(self.charset)

class AnsiTextRenderer(PlainTextRenderer):

    media_type = 'text/plain'
    format = 'ansi'
