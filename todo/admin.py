from django.contrib import admin
from .models import Item

# Register your models here.
# Expose the Item class to the Django admin interface
admin.site.register(Item)
