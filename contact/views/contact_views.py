from django.shortcuts import render
from contact.models import Contact

def find_all_contact(request):
    contacts = Contact.objects.all().order_by('id').filter(show=True)
    return render(request, 'contact/index.html', context = {'contacts': contacts})

def find_contact_by_id(request, contact_id):
    single_contact = Contact.objects.filter(id=contact_id).first()
    return render(request, 'contact/contact.html', context={'contact': single_contact})