from django.contrib import admin
from .models import Reference, Photo


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 50
    fields = ('image', 'alt_text')

@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = [PhotoInline]

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('reference', 'id', 'created_at')
    list_filter = ('reference',)
