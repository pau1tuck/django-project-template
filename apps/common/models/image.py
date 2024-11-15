# apps/common/models/image.py
from django.db import models

from apps.common.models import Upload

ACCEPTED_FILE_TYPES = ["jpg", "gif", "png"]


class Image(Upload, models.Model):
    thumbnail_url = models.URLField(default="", null=True, blank=True)

    # INCLUDED BY MIXINS
    # url = str
    # id = uuid
    # meta_data = dict
    # created_at = datetime
    # modified_at = datetime

    # MODEL PROPERTIES
    @property
    def width(self):
        if self.is_image:
            return (
                self.meta_data["meta"].get("width")
                if self.meta_data.get("meta")
                else None
            )

    @property
    def height(self):
        if self.is_image:
            return (
                self.meta_data["meta"].get("height")
                if self.meta_data.get("meta")
                else None
            )
