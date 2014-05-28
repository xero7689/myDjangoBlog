# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Album'
        db.create_table('work_album', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('work', ['Album'])

        # Adding model 'Tag'
        db.create_table('work_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('work', ['Tag'])

        # Adding model 'Image'
        db.create_table('work_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=60)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('filename', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=100)),
        ))
        db.send_create_signal('work', ['Image'])

        # Adding M2M table for field tags on 'Image'
        m2m_table_name = db.shorten_name('work_image_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('image', models.ForeignKey(orm['work.image'], null=False)),
            ('tag', models.ForeignKey(orm['work.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['image_id', 'tag_id'])

        # Adding M2M table for field albums on 'Image'
        m2m_table_name = db.shorten_name('work_image_albums')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('image', models.ForeignKey(orm['work.image'], null=False)),
            ('album', models.ForeignKey(orm['work.album'], null=False))
        ))
        db.create_unique(m2m_table_name, ['image_id', 'album_id'])


    def backwards(self, orm):
        # Deleting model 'Album'
        db.delete_table('work_album')

        # Deleting model 'Tag'
        db.delete_table('work_tag')

        # Deleting model 'Image'
        db.delete_table('work_image')

        # Removing M2M table for field tags on 'Image'
        db.delete_table(db.shorten_name('work_image_tags'))

        # Removing M2M table for field albums on 'Image'
        db.delete_table(db.shorten_name('work_image_albums'))


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
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'filename': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['work.Tag']"}),
            'title': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '60'}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'work.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['work']