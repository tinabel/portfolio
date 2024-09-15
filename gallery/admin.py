from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin
from django.contrib import admin
from .models import Image, Series, Medium, Page
from import_export import resources
from django import forms

class SeriesResource(resources.ModelResource):
  class Meta:
    model = Series
    import_id_fields = ['title', 'slug', 'cover_image']
    skip_unchanged = True
    use_bulk = True

class SeriesAdmin(ImportExportActionModelAdmin):
  resource_class = SeriesResource
  list_display = ('title', 'slug', 'cover_image')
  prepopulated_fields = {'slug': ('title',)}

admin.site.register(Series, SeriesAdmin)

class MediumAdmin(admin.ModelAdmin):
  list_display = ('name', 'slug', 'cover_image')
  prepopulated_fields = {"slug": ("name")}

class MediumResource(resources.ModelResource):
  class Meta:
    model = Medium
    import_id_fields = ['name', 'cover_image', 'slug']
    skip_unchanged = True
    use_bulk = True

  def get_description(self):
    return self.description

class MediumAdmin(ImportExportActionModelAdmin):
  resource_class = MediumResource
  list_display = ('name', 'slug', 'cover_image')
  prepopulated_fields = {'slug': ('name',)}

admin.site.register(Medium, MediumAdmin)

class ImageResource(resources.ModelResource):
    class Meta:
        model = Image
        import_id_fields = ['image_file', 'title', 'alt', 'description', 'medium', 'series', 'tags', 'is_featured']
        skip_unchanged = True
        use_bulk = True

class ImageAdmin(ImportExportActionModelAdmin):
  resource_class = ImageResource
  fields = ('title', 'image_tag', 'image_file', 'thumbnail_image', 'slug', 'alt', 'description', 'medium', 'series', 'tags', 'is_featured', 'image_focal_point')
  list_display = ('title', 'image_file', 'thumbnail_image', 'slug', 'alt', 'description', 'medium', 'series', 'tags', 'is_featured')
  list_filter = ('medium', 'series')
  prepopulated_fields = {'slug': ('title',)}
  readonly_fields = ('image_tag',)

  def get_description(self):
    return self.description

admin.site.register(Image, ImageAdmin)


class PageResource(resources.ModelResource):
    class Meta:
        model = Page
        import_id_fields = [ 'title', 'date', 'content', 'slug']
        skip_unchanged = True
        use_bulk = True

class PageAdmin(ImportExportActionModelAdmin):
  resource_class = PageResource
  fields = ('title', 'content', 'slug')
  list_display = ('title', 'date', 'slug',)
  list_filter = ('title', 'date', 'slug')
  prepopulated_fields = {'slug': ('title',)}

  def get_description(self):
    return self.description

admin.site.register(Page, PageAdmin)

