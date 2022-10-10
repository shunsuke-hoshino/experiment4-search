from django.shortcuts import render
from django.http import HttpResponse
from .forms import SearchForm
from .models import Word
from search import found

# Create your views here.

def index(request):
    searchname = ''
    if(request.method == 'POST'):
        form = SearchForm(request.POST)
        searchname = form['searchname'].data or '' #searchnameはindex.htmlの<input type = "text" name="searchname">と対応している
        print(str(searchname))
    if(searchname != ''):
        data = Word(word=searchname)
        data.save()
        teachname = found.search(searchname)
    
    datalist = Word.objects.all()
    params = {
        'title':'検索サイト',
        'data':datalist,
        #'teachname':data1,
    }
    print(datalist)
    return render(request, 'index.html',params)