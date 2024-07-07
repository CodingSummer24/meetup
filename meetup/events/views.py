from django.shortcuts import render
from .models import Group


def home(request):
    groups = Group.objects.all()
    return render(request, 'home.html', {'groups': groups})


def group_page(request, slug):
    try:
        group = Group.objects.get(slug = slug)
    except:
        return render(request, 'error.html', {'message': 'Group ' + slug + ' not found'})
    return render(request, 'group.html', {'group': group})
