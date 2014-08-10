from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from mainstay.models import UpdatedAndCreated


class Directory(MPTTModel, UpdatedAndCreated):
    name = models.CharField(max_length=200)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        self._set_update_and_created()
        return super(Directory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class File(UpdatedAndCreated, models.Model):
    name = models.CharField(max_length=200)
    file = models.FileField()
    directory = TreeForeignKey('Directory', null=True, blank=True, related_name='files')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
