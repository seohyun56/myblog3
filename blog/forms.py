from django import forms
from .models import Blog
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib.auth.models import User


class CreateBlog(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = []
        files = ['title', 'writer', 'content']

        widgets = {
            'title' : forms.TextInput(
                attrs={'class':'form-control', 'sytle':'width:500', 'placeholder':'제목을 입력하세요.'}
            ),
            'writer' : forms.Select(
                attrs={'class':'custom-select'}
            ),
            'contents' : forms.CharField(widget=CKEditorUploadingWidget()),
        }

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']