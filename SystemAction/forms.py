# encoding: utf-8
from django import forms



class SaveForm(forms.Form):
    book_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    book_name.label = u"书籍名称"

    author = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    author.label =u"作者名称"

    press = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    press.label = u"出版社"

    publication_year = forms.CharField(max_length=4,widget=forms.TextInput(attrs={'class': 'form-control'}))
    publication_year.label= u"出版年份"

    introduction = forms.TextInput(attrs={'class':'form-control'})


