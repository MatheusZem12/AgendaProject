from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    show = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return f'{self.id} - {self.name}'
    
    class Meta():
        db_table = 'tb_category'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=122)
    created_date = models.DateField(default=timezone.now)
    description = models.TextField()
    show = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='pictures/%Y/%m', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self) -> str:
        return f'{self.id} - {self.first_name} {self.last_name}'
    
    class Meta():
        db_table = 'tb_contact'