from django import forms
from .models import Post
class homeForm(forms.ModelForm):
    post = forms.CharField()
    class Meta:
        model = Post
        fields = ['post']
