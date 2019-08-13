from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    if request.GET.get('sort') == 'name':
        phone_set = Phone.objects.order_by('name')
        context = {'phones' : phone_set}
    elif request.GET.get('sort') == 'min_price':
        phone_set = Phone.objects.order_by('price')
        context = {'phones' : phone_set}
    elif request.GET.get('sort') == 'max_price':
        phone_set = Phone.objects.order_by('-price')
        context = {'phones' : phone_set}
    else:
        phone_set = Phone.objects.all()
        context = {'phones' : phone_set}
        print(context)
    
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    for phone in Phone.objects.all():
        if phone.slug == slug:
            context = {'phone' : phone}
    return render(request, template, context)
