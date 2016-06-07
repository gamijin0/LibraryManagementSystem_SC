# encoding: utf-8
from django import forms


#  表单内容
class SaveForm(forms.Form):


    book_id = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class': 'form-control'}))
    book_id.label = u"书籍编号"
    book_id.error_messages={'required':'请输入书籍编号'}

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

    category_id = forms.CharField(max_length=4, widget=forms.TextInput(attrs={'class': 'form-control'}))
    category_id.label = u"类型"
    category_id.error_messages = {'required': '请输入书本类型'}

    inventory = forms.IntegerField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    inventory.label = u"入库数量"
    inventory.error_messages = {'required': '请输入入库数量'}



