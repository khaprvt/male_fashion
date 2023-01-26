from django import forms

from products.models import ColorModel


class AddColorForm(forms.ModelForm):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'color'
    }))

    class Meta:
        model = ColorModel
        fields = ['code']
