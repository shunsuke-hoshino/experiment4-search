from django.shortcuts import render
from django.http import HttpResponse
from .forms import SearchForm
from .models import Word
from search import found
import pandas

# Create your views here.

def index(request):
    searchname = ''
    teachname = []
    c = 0
    if(request.method == 'POST'):
        form = SearchForm(request.POST)
        searchname = form['searchname'].data or '' #searchnameはindex.htmlの<input type = "text" name="searchname">と対応している
        # print(str(searchname))
    if(searchname != ''):
        data = Word(word=searchname)
        data.save()
        teachname = found.search(searchname)
        # print(teachname[1])
        # print(teachname[2])
        #for x in teachname:
        #   print(x)
    
    if(teachname == 0):
        teachname = ["見つかりませんでした。"]
    
    datalist = Word.objects.all()
    print(type(datalist))
    countlist = Word.objects.values()
    print(countlist)
    #countlist = Word.objects.all().filter(word = searchname)
    #for x in countlist:
        #print(str(x))
        #c += 1
        #if(c >= 10){
        #    Word(hotword = searchname)
        #}

    
    params = {
        'title':'福岡工業大学教授検索サイト',
        'data':datalist,
        'name':teachname,
    }
    return render(request, 'index.html',params)