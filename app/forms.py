from django import forms
from .models import Item


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('name', 'no', 'category', 'gauge', 'release_condition', 'range', 'continuous_power', 'fixed_num',)
        widgets = {
                    'name': forms.TextInput(),
                    'no': forms.NumberInput(attrs={'min': 1}),
                    'category': forms.RadioSelect(),
                    'gauge': forms.NumberInput(attrs={'min': 0}),
                    'release_condition': forms.NumberInput(attrs={'min': 0}),
                    'range': forms.NumberInput(attrs={'min': 0}),
                    'continuous_power': forms.NumberInput(attrs={'min': 0}),
                    'fixed_num': forms.NumberInput(attrs={'min': 0}),
                  }
