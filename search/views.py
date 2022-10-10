from django.shortcuts import render
from django.http import HttpResponse
from .forms import SearchForm
from .models import Word

# Create your views here.

def index(request):
    form = SearchForm(request.POST)
    searchname = form['searchname'].data or ''
    print(str(searchname))
    if(searchname != ''):
        data = Word(word=searchname)
        data.save()
    
    datalist = Word.objects.all()
    params = {
        'title':'検索サイト',
        'data':datalist,
    }
    return render(request, 'index.html',params)