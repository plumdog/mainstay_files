from django.conf.urls import patterns, url
from . import views

PREFIX = 'files'

urlpatterns = patterns(
    '',
    url(r'^/$', views.index, name='index'),
    url(r'^/add-directory/$', views.AddDirectory.as_view(), name='add_directory'),
    url(r'^/edit-directory/(?P<directory_id>[0-9]+)/$', views.EditDirectory.as_view(), name='edit_directory'),

    url(r'^/directory/(?P<directory_id>[0-9]+)/$', views.directory, name='directory'),
    url(r'^/add-file/$', views.add_file, name='add_file'),
    url(r'^/edit-file/(?P<file_id>[0-9]+)/$', views.edit_file, name='edit_file'),
    url(r'^/download-file/(?P<file_id>[0-9]+)/$', views.download_file, name='download_file'))
