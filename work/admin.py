from django.contrib import admin
from work.models import Album, Tag, Image

# Register your models here.
class AlbumAdmin(admin.ModelAdmin):
	search_fields = ["title"]
	list_display = ["title", "images"]

class TagAdmin(admin.ModelAdmin):
	list_display = ["tag"]

class ImageAdmin(admin.ModelAdmin):
	search_fields = ["title"]
	list_display = ["__unicode__", "title", "size",
		"tags_", "albums_","thumbnail", "created"]
	list_filter = ["tags", "albums"]

admin.site.register(Album, AlbumAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Image, ImageAdmin)
