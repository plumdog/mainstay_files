from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper

import os

from mimetypes import guess_type

from .forms import DirectoryForm, FileForm
from .models import Directory, File
from mainstay.crud import MainstayCreateView, MainstayUpdateView


def _for_directory(request, directory_id):
    if directory_id is not None:
        directory = get_object_or_404(Directory, id=directory_id)
    else:
        directory = None
    directories = Directory.objects.filter(parent_id=directory_id).all()
    files = File.objects.filter(directory_id=directory_id).all()
    return render(request, 'mainstay_files/index.html',
                  {'directories': directories, 'files': files})


def index(request):
    return _for_directory(request, None)


def directory(request, directory_id):
    return _for_directory(request, directory_id)


class AddDirectory(MainstayCreateView):
    template_name = 'mainstay_files/add_directory.html'
    form_class = DirectoryForm
    reverse_success_url = 'mainstay_files:index'
    success_message = 'Directory added'


class EditDirectory(MainstayUpdateView):
    template_name = 'mainstay_files/edit_directory.html'
    model = Directory
    form_class = DirectoryForm
    reverse_success_url = 'mainstay_files:index'
    success_message = 'Directory updated'
    pk_url_kwarg = 'directory_id'


def add_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'File added')
            return redirect('mainstay_files:index')
        else:
            messages.error(request, 'Errors')
    else:
        form = FileForm()

    return render(request, 'mainstay_files/add_file.html', {'form': form})    


def edit_file(request, file_id):
    file_ = get_object_or_404(File, id=file_id)
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES, instance=file_)
        if form.is_valid():
            form.save()
            messages.success(request, 'File editted')
            return redirect('mainstay_files:index')
        else:
            messages.error(request, 'Errors')
    else:
        form = FileForm(instance=file_)

    return render(request, 'mainstay_files/edit_file.html', {'form': form})

def download_file(request, file_id):
    file_ = get_object_or_404(File, id=file_id)
    path = file_.file.url
    response = HttpResponse(content_type=guess_type(path))
    response['X-Sendfile'] = path
                            
    response['Content-Disposition'] = 'attachment; filename=' + file_.name
    return response
    
