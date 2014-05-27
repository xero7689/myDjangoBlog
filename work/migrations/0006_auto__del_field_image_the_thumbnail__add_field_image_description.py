# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Image.the_thumbnail'
        db.delete_column('work_image', 'the_thumbnail')

        # Adding field 'Image.description'
        db.add_column('work_image', 'description',
                      self.gf('django.db.models.fields.TextField')(blank=True, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Image.the_thumbnail'
        db.add_column('work_image', 'the_thumbnail',
                      self.gf('django.db.models.fields.files.ImageField')(blank=True, null=True, max_length=100),
                      keep_default=False)

        # Deleting field 'Image.description'
        db.delete_column('work_image', 'description')


    models = {
        'work.album': {
            'Meta': {'object_name': 'Album'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'work.image': {
            'Meta': {'object_name': 'Image'},
            'albums': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['work.Album']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['work.Tag']"}),
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