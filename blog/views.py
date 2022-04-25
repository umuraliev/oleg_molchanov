from django.http import HttpResponse
from django.shortcuts import render


def posts_list(request):
    n = ['Rus', 'Nick', 'John', 'Sam']
    return render(request, 'blog/index.html', context={'names': n})
