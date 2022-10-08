from django import forms

class SearchForm(forms.Form):
    searchname = forms.CharField(label = 'キーワード')