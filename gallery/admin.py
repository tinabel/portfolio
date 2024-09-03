from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin
from django.contrib import admin
from .models import Image, Series, Medium
from import_export import resources

admin.site.register(Series)

class SeriesAdmin(admin.ModelAdmin):
  list_display = ('title', 'slug', 'cover_image')
  prepopulated_fields = {"slug": ("title")}

admin.site.register(Medium)

class MediumAdmin(admin.ModelAdmin):
  list_display = ('name', 'slug', 'cover_image')
  prepopulated_fields = {"slug": ("name")}


class ImageResource(resources.ModelResource):
    class Meta:
        model = Image
        import_id_fields = ["image_file", "title", "alt", "description", "medium", "series", "tags", "is_featured"]
        skip_unchanged = True
        use_bulk = True

class ImageAdmin(ImportExportActionModelAdmin):
  resource_class = ImageResource
  list_display = ('title', 'image_file', 'slug', 'alt', 'description', 'medium', 'series', 'tags', 'is_featured')
  list_filter = ('medium', 'series')
  prepopulated_fields = {"slug": ("title",)}

  def get_description(self):
    return self.description

admin.site.register(Image, ImageAdmin)