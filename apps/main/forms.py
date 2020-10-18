from django import forms

class ImageForm(forms.Form):
    img = forms.ImageField()
    numero_identificatorio = forms.CharField()