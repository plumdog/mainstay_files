from django.forms import ModelForm, Form, CharField

from .models import Directory, File

class DirectoryForm(ModelForm):
    class Meta:
        model = Directory
        fields = ['name', 'parent']


class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ['name', 'file', 'directory']
