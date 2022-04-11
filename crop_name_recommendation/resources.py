from import_export import resources
from .models import FarmData

class FarmDataResource(resources.ModelResource):
    class Meta:
        model = FarmData