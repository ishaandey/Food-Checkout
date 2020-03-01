from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime

from .forms import ItemForm
from .models import Item
from django.http import HttpResponseRedirect


def index(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            Item(item_name = form.cleaned_data['item_name'],
                comment = form.cleaned_data['comment'],
                owner = request.user,
                exp_date = form.cleaned_data['exp_date'],
                ).save()
            return HttpResponseRedirect('/')

    else:
        form = ItemForm()

    items = Item.objects.all().order_by('-ts_added')
    user_web_url = 'https://www.google.com/'
    food_url = ''
    return render(request, 'index.html', {'form': form, 'items':items, 'url1':user_web_url})

@login_required
def about(request):
    return render(request, 'about.html')

