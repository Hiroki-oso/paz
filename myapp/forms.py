from django import forms
from .models import Person

class FirstForm(forms.ModelForm):
    username = forms.CharField(label='お名前')
    height = forms.FloatField(label='身長')
    weight = forms.IntegerField(label='体重')
    memo = forms.CharField(label='memo')
    
    class Meta:
        model = Person
        fields = ('height', 'weight', 'username', 'memo',)
