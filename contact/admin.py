from django.contrib import admin
from contact.models import Contact, Category

# Register your models here.
@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = 'id', 'name', 'description', 'show',
    ordering = 'id',
    search_fields = 'name', 'description',
    list_filter = 'show',
    list_per_page = 10
    list_max_show_all = 100

@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'email', 'created_date', 'description', 'show', 'picture',
    ordering = 'id',
    search_fields = 'first_name', 'last_name', 'email',
    list_filter = 'show', 'created_date',
    list_per_page = 10
    list_max_show_all = 100
    list_editable = 'show',