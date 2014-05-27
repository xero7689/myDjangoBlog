from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from redactor.fields import RedactorField
# Create your models here.

class postTag(models.Model):
    tagName = models.CharField(max_length=50)
    def __unicode__(self):
        return self.tagName

    def get_absolute_url(self):
        return reverse('blog.views.tag', args=[self.tagName])
    
    def get_manyTomany_numb(self):
        return self.post_tags.all().count()
    
    def tag_font_size(self):
        fontSize = self.get_manyTomany_numb() * 15
        return fontSize

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.CharField(max_length=255)
    content = RedactorField(
          verbose_name='Text',
          upload_to='uploads/',
          allow_file_upload=True,
          allow_image_upload=True,)
    #models.TextField(verbose_name='postContent', blank=True)
    #content2 = RedactorField(verbose_name='Text')
    published = models.BooleanField(default=True)
    created = models.DateTimeField()
    tags = models.ManyToManyField(postTag, related_name='post_tags', blank=True)
    
    class Meta:
	    ordering= ["-created"]
    
    def __unicode__(self):
	    return u'%s' % self.title
    
    def get_absolute_url(self):
        return reverse('blog.views.post', args=[self.slug])

class Contact(models.Model):
	name = models.CharField(max_length=60)
	email = models.EmailField(max_length=75)
	created = models.DateTimeField(auto_now_add=True)
	comment = models.TextField()
