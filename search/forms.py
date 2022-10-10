from django import forms

class SearchForm(forms.Form):
    searchname = forms.CharField(
        max_length = 100,
        required = True,
    )