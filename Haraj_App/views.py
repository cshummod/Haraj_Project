from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ItemForm, UserForm, ProfileForm, LoginForm
from .models import Item
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('home'))
                else:
                    messages.error(request, 'user is not active')
            else:
                messages.error(request, 'invalid username or password')
    data = {'form': form}
    return render(request, 'login.html', data)


def register(request):
    userForm = UserForm()
    profileForm = ProfileForm()

    if request.method == 'POST':
        userForm = UserForm(request.POST)
        profileForm = ProfileForm(request.POST)

        if userForm.is_valid() and profileForm.is_valid():
            user = userForm.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile = profileForm.save(commit=False)
            profile.user = user
            profile.save()
            return HttpResponseRedirect(reverse('home'))
    data = {
        'userForm': userForm,
        'profileForm': profileForm
    }

    return render(request, 'register.html', data)


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    data = {
        'item': item
    }
    return render(request, 'detail.html', data)


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
