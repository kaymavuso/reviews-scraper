from django.db import models
import uuid
from profiles.models import Profile

# Create your models here.

class Job(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user_id = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200, null=False)
    selected_store = models.CharField(max_length=200, null=False)
    selected_brand = models.CharField(max_length=200, null=False)
    selected_product = models.CharField(max_length=200, null=False)
    product_image = models.ImageField(null=True, blank=True, default="default.jpg")
    status = models.CharField(max_length=1, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    tm_stamp = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
