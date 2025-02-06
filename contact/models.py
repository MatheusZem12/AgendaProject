from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'tb_category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return f'{self.name}'


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/', null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    
    class Meta:
        db_table = 'tb_contact'

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
    def name(self) -> str:
        return f'{self.first_name} {self.last_name}'