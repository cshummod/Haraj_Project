from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ItemForm
from .models import Item
from django.contrib import messages
from django.urls import reverse


def index(request):
    items = Item.objects.all()
    data = {
        'items': items
    }
    return render(request, 'index.html', data)


def add_item(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            if 'picture' in request.FILES:
                item.picture = request.FILES['picture']
            item.save()
            messages.success(request, 'your item has been added sucessfully')
            return HttpResponseRedirect(reverse('home'))
    data = {
        'form': form
    }

    return render(request, 'add_item.html', data)
