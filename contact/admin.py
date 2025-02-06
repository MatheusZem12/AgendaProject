from django.contrib import admin
from contact.models import Contact, Category

# Register your models here.
@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = 'id', 'name'
    ordering = 'id',
    list_per_page = 10
    list_max_show_all = 100

@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'owner', 'show'
    list_editable = 'show',
    ordering = 'id',
    search_fields = 'first_name', 'last_name'
    list_per_page = 10
    list_max_show_all = 100