from django import forms
from django.forms import ModelForm

from apps.post.models import *


class FormNew(ModelForm):
    def __init__(self, *args, **kwargs):
        for f in self.base_fields:
            self.base_fields[f].widget.attrs['class'] = 'form-control'
            self.base_fields[f].widget.attrs['title'] = self.base_fields[f].label
            self.base_fields[f].widget.attrs['placeholder'] = self.base_fields[f].label
            self.base_fields[f].widget.attrs['data-toggle'] = 'tooltip'
        super(FormNew, self).__init__(*args, **kwargs)

    class Meta():
        model = Notice
        fields = '__all__'
        exclude = ['author']




