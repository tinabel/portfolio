from import_export import resources
from .models import Image

class ImageResource(resources.ModelResource):

    class Meta:
        model = Image
        import_id_fields = ["image_file", "title", "alt", "description", "medium", "series", "tags", "is_featured"]
        skip_unchanged = True
        use_bulk = True