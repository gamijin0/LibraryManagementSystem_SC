# encoding: utf-8
from django import forms



class SaveForm(forms.Form):
    book_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    book_name.label = u"书籍名称"
    book_name.error_messages={'required':'请输入书籍名称'}

    author = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    author.label =u"作者名称"
    author.error_messages={'required':'请输入作者名称'}

    press = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    press.label = u"出版社"
    press.error_messages = {'required': '请输入出版社'}

    publication_year = forms.CharField(max_length=4,widget=forms.TextInput(attrs={'class': 'form-control'}))
    publication_year.label= u"出版年份"
    publication_year.error_messages = {'required': '请输入出版年份'}

    add_time = forms.CharField(max_length=4, widget=forms.TextInput(attrs={'class': 'form-control'}))
    add_time.label = u"上架时间"
    add_time.error_messages = {'required': '请输入上架时间'}

    category_id = forms.CharField(max_length=4, widget=forms.TextInput(attrs={'class': 'form-control'}))
    category_id.label = u"类型"
    category_id.error_messages = {'required': '请输入书本类型'}

    counts = forms.IntegerField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    counts.label = u"入库数量"
    counts.error_messages = {'required': '请输入入库数量'}

    introduction = forms.TextInput(attrs={'class': 'form-control'})


