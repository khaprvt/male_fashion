from django import forms
from .models import CommentModel

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = CommentModel
        exclude = ['created_at', 'blog']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Name'}),
            'email': forms.EmailInput(attrs={'placeholder':'Email'}),
            'phone': forms.TextInput(attrs={'placeholder':'Phone'}),
            'comment': forms.Textarea(attrs={'placeholder':'Comment'}),
        }