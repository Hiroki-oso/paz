from django import forms
from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

class UserCreationForm(forms.ModelForm):
    password = forms.CharField()
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password',)
        
    def clean_password(self):
        password = self.cleaned_data.get("password")
        return password
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    
class SignupForm(forms.ModelForm):
    username = forms.CharField(label='お名前')
    email = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def save(self, commit=False):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user
    
class UserLoginForm(AuthenticationForm):
    # class Meta:
    #     model = Users
    #     fields = ['email', 'password']
    username = forms.EmailField(label='メールアドレス', widget=forms.PasswordInput())
    password = forms.CharField(label='パスワード')
    remember = forms.BooleanField(label='ログイン状態を保持', required=False)