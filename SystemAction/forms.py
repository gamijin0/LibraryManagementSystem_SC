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

    add_time = forms.CharField(max_length=4, widget=forms.TextInput(attrs={'class': 'form-control'}))
    add_time.label = u"上架时间"

    category_id = forms.CharField(max_length=4, widget=forms.TextInput(attrs={'class': 'form-control'}))
    category_id.label = u"类型"

    counts = forms.CharField(max_length=4, widget=forms.TextInput(attrs={'class': 'form-control'}))
    counts.label = u"入库数量"

    introduction = forms.TextInput(attrs={'class':'form-control'})

