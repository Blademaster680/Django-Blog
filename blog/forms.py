from django import forms
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Post


class PostCreateForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=SummernoteWidget)

    class Meta:
        model = Post
        fields = ['title', 'content']


class PostUpdateForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=SummernoteWidget)

    class Meta:
        model = Post
        fields = ['title', 'content']