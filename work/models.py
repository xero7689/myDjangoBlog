from django.db import models
from django.contrib.auth.models import User
from PIL import Image as PImage
from blog2.settings import MEDIA_ROOT
import os
import io

# Create your models here.

class Album(models.Model):
	title = models.CharField(max_length=60)
	public = models.BooleanField(default=False)
	def __unicode__(self):
		return self.title
	def images(self):
		lst = [x.image.name for x in self.image_set.all()]
		lst = ["<a href='/media/%s'>%s</a>" % (x, x.split('/')[-1]) for x in lst]
		return ', '.join(lst)
	images.allow_tags = True

class Tag(models.Model):
	tag = models.CharField(max_length=50)
	def __unicode__(self):
		return self.tag
		
class Image(models.Model):
	title = models.CharField(max_length=60, blank=True, null=True)
	image = models.ImageField(upload_to="mywork/") #/mywork/ should be a variable
	tags = models.ManyToManyField(Tag, blank=True)
	albums = models.ManyToManyField(Album, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	width = models.IntegerField(blank=True, null=True)
	height = models.IntegerField(blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	filename = models.CharField(max_length=100, blank=True, null=True)
	
	def __unicode__(self):
		return self.image.name
	
	def save(self, *args, **kwargs):
		"""save image dimensions"""
		"""Overriding predefined model methods"""
		super(Image, self).save(*args, **kwargs) #call the "real" save method
		im = PImage.open(os.path.join(MEDIA_ROOT, self.image.name))
		self.width, self.height = im.size
		
		"""create thumbnail"""
		im.thumbnail((320, 320), PImage.ANTIALIAS)
		thum_fn = os.path.join(MEDIA_ROOT, "mywork/thumbnail/" + self.image.name[7:])
		im.save(thum_fn, "JPEG")
		
		"""set filename"""
		self.filename = self.image.name[7:]
		
		super(Image, self).save(*args, **kwargs) #call the "real" save method
		

	def size(self):
		return "%s x %s" % (self.width, self.height)
	
	def __unicode__(self):
		return self.image.name
	
	def tags_(self):
		lst = [x[1] for x in self.tags.values_list()]
		return ', '.join(lst)
	def albums_(self):
		lst = [x[1] for x in self.tags.values_list()]
		return ', '.join(lst)
		
	def thumbnail(self):
		return '<a href="/media/%s"><img  border="0" src="/media/%s" height="90" ></a>' % (self.image.name, self.image.name)
	thumbnail.allow_tags = True #important!!
