# forms.py
from django import forms
from .models import Article
from .models import Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']  
        widgets = {
            'author': forms.HiddenInput(),  
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
