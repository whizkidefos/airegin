from django.contrib import admin

from .models import Listing

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'city', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor', 'city')
    list_editable = ('is_published', )
    search_fields = ('city', 'title', 'description', 'state', 'zipcode', 'price', 'address')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)
