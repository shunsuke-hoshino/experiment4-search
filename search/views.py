from django.shortcuts import render
from django.http import HttpResponse
from .forms import SearchForm

# Create your views here.

def index(request):
    params = {
        'title':'検索サイト',
        'form': SearchForm(),
    }
    if(request.method == 'POST'):
        params['form'] = SearchForm(request.POST)
        a = SearchForm(request.POST)
        print(a)
    return render(request, 'index.html',params)