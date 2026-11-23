from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Note, NoteLink


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category")
    search_fields = ("title", "content")
    list_filter = ("category",)


@admin.register(NoteLink)
class NoteLinkAdmin(admin.ModelAdmin):
    list_display = ("source", "relationship", "target")
    list_filter = ("relationship",)
