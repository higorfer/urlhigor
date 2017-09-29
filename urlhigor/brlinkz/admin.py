from django.contrib import admin
from .models import Urls


class UrlsAdmin(admin.ModelAdmin):
    list_display = ('short_id','httpurl','pub_date', 'count', 'fav')
    ordering = ('-pub_date',)


admin.site.register(Urls, UrlsAdmin)