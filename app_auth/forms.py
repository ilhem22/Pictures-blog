from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Nom utilisateur" ,widget=forms.TextInput(attrs={'class': 'my-class','id': 'my-id',}),)
    pwd = forms.CharField(label="Mot de passe" ,widget=forms.PasswordInput(attrs={'class':'my-class'}))
    

class RegisterForm(forms.Form):
    username = forms.CharField(label="Nom utilisateur" ,widget=forms.TextInput(attrs={'class': 'my-class','id': 'my-id',}),)
    pwd = forms.CharField(label="Mot de passe" ,widget=forms.PasswordInput(attrs={'class':'my-class'}))
    pwd_confirm = forms.CharField(label="Mot de passe de confirmation" ,widget=forms.PasswordInput(attrs={'class':'my-class'}))
