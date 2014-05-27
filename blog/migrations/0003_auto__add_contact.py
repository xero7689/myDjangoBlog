# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contact'
        db.create_table('blog_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('comment', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('blog', ['Contact'])


    def backwards(self, orm):
        # Deleting model 'Contact'
        db.delete_table('blog_contact')


    models = {
        'blog.contact': {
            'Meta': {'object_name': 'Contact'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'blog.post': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Post'},
            'content': ('redactor.fields.RedactorField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'unique': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'post_tags'", 'symmetrical': 'False', 'to': "orm['blog.postTag']", 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'blog.posttag': {
            'Meta': {'object_name': 'postTag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tagName': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['blog']