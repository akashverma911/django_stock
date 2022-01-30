from django import forms

class SymbolForm(forms.Form):
    symbol = forms.CharField(label='Enter Symbol', max_length=100)
