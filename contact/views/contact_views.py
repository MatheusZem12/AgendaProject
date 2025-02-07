from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from contact.models import Contact
from django.db.models import Q
from django.core.paginator import Paginator

def find_all_contact(request):
    contacts = Contact.objects.filter(show=True).order_by('id')
    paginator = Paginator(contacts, 10)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(request, 'contact/index.html', context = {'page_obj': page_obj})

def search_contact(request):
    search = request.GET.get('q','')
    if search:
        redirect('contact:index')
    contacts = Contact.objects.filter(
        Q(first_name__icontains=search) |
        Q(id__icontains=search)
    )
    paginator = Paginator(contacts, 10)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(request, 'contact/index.html', context = {'page_obj': page_obj})


def find_contact_by_id(request, contact_id):
    single_contact = get_object_or_404(Contact, id=contact_id)
    return render(request, 'contact/contact.html', context={'contact': single_contact})