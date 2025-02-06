from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.find_all_contact, name= 'index'),
    path('<int:contact_id>/', views.find_contact_by_id, name='contact')
]

