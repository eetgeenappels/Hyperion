from django import forms


class Prompt(forms.Form):
    prompt = forms.CharField(label='Prompt', max_length=500)
