from django.contrib import admin

# Register your models here.

from .models import Headline, Text

admin.site.register(Headline)
admin.site.register(Text)