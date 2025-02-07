from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from contact.models import Contact
from django.db.models import Q

def find_all_contact(request):
    contacts = Contact.objects.order_by('id').filter(show=True)
    return render(request, 'contact/index.html', context = {'contacts': contacts})

def search_contact(request):
    search = request.GET.get('q','')
    if search:
        redirect('contact:index')
    print(search)
    contacts = Contact.objects.filter(
        Q(first_name__icontains=search) |
        Q(id__icontains=search)
    )
    print(contacts.query)
    return render(request, 'contact/index.html', context = {'contacts': contacts})


def find_contact_by_id(request, contact_id):
    single_contact = get_object_or_404(Contact, id=contact_id)
    return render(request, 'contact/contact.html', context={'contact': single_contact})