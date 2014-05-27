from django.contrib import admin
from blog.models import postTag, Post, Contact
from django.forms import ModelForm
from django.contrib.admin import ModelAdmin

# Register your models here.


class postAdmin(ModelAdmin):
    list_display = ('title', 'created', 'published')
    search_fields = ('title',)
    
class postTagAdmin(ModelAdmin):
	list_display = ('tagName',)
	search_fields = ('tagName',)
	
class contactAdmin(ModelAdmin):
	list_display = ('name', 'email', 'created', 'comment')

admin.site.register(postTag, postTagAdmin)
admin.site.register(Post, postAdmin)
admin.site.register(Contact, contactAdmin)

