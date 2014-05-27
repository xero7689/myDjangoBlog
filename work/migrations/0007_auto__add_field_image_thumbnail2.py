# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Image.thumbnail2'
        db.add_column('work_image', 'thumbnail2',
                      self.gf('django.db.models.fields.files.ImageField')(blank=True, null=True, max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Image.thumbnail2'
        db.delete_column('work_image', 'thumbnail2')


    models = {
        'work.album': {
            'Meta': {'object_name': 'Album'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'work.image': {
            'Meta': {'object_name': 'Image'},
            'albums': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['work.Album']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['work.Tag']"}),
            'thumbnail2': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '60'}),
            'width': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'work.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['work']