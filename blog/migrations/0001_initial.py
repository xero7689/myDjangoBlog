# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'postTag'
        db.create_table('blog_posttag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tagName', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('blog', ['postTag'])

        # Adding model 'Post'
        db.create_table('blog_post', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, unique=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content', self.gf('redactor.fields.RedactorField')()),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('blog', ['Post'])

        # Adding M2M table for field tags on 'Post'
        m2m_table_name = db.shorten_name('blog_post_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm['blog.post'], null=False)),
            ('posttag', models.ForeignKey(orm['blog.posttag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['post_id', 'posttag_id'])

        # Adding model 'Contact'
        db.create_table('blog_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('blog', ['Contact'])


    def backwards(self, orm):
        # Deleting model 'postTag'
        db.delete_table('blog_posttag')

        # Deleting model 'Post'
        db.delete_table('blog_post')

        # Removing M2M table for field tags on 'Post'
        db.delete_table(db.shorten_name('blog_post_tags'))

        # Deleting model 'Contact'
        db.delete_table('blog_contact')


    models = {
        'blog.contact': {
            'Meta': {'object_name': 'Contact'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['blog.postTag']", 'related_name': "'post_tags'", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'blog.posttag': {
            'Meta': {'object_name': 'postTag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tagName': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['blog']