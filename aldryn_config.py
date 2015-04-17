# -*- coding: utf-8 -*-
from aldryn_client import forms


class Form(forms.BaseForm):
    write_key = forms.CharField('API Key (write key)', max_length=200)

    def to_settings(self, data, settings):
        settings['SEGMENT_WRITE_KEY'] = data['write_key']
        return settings
