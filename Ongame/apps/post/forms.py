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


class FormImg(ModelForm):
    def __init__(self, *args, **kwargs):
        notice = Notice.objects.all()
        lista = []
        for i in notice:
            lista.append(i.title)
        for f in self.base_fields:
            self.base_fields[f].widget.attrs['class'] = 'form-control'
            self.base_fields[f].widget.attrs['title'] = self.base_fields[f].label
            self.base_fields[f].widget.attrs['placeholder'] = self.base_fields[f].label
            self.base_fields[f].widget.attrs['data-toggle'] = 'tooltip'
        super(FormImg, self).__init__(*args, **kwargs)

    class Meta():
        model = Image
        fields = 'title_img', 'description', 'sequence'



