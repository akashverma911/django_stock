from django.contrib import admin

from .models import Common, Share, SmeEquity

# Register your models here.
admin.site.register(SmeEquity)
admin.site.register(Share)
admin.site.register(Common)

