from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,SetPasswordForm,PasswordResetForm
from django.contrib.auth.models import User


from .models import Customer

class formularioiniciosesión(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'form-control'}))

class formularioregistroclientes(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    email= forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1= forms.CharField(label='Contraseña',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2= forms.CharField(label='Confirmar contraseña',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Contraseña antigua',widget=forms.PasswordInput(attrs={'autofocus':'true','autocomplete':'current-password', 'class':'form-control'}))
    new_password1 = forms.CharField(label='Nueva contraseña',widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))
    new_password2 = forms.CharField(label='Confirmar nueva contraseña',widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))



class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))


class MySetPasswordForm(SetPasswordForm):
   
    new_password1= forms.CharField (label='Nueva contraseña', widget=forms.PasswordInput(attrs={'autocomplete' : 'current-password', 'class ':'form-control'}))
    new_password2= forms.CharField (label='Confirmar nueva contraseña', widget=forms.PasswordInput(attrs={'autocomplete' : 'current-password','Class': 'form-control'}))
    


class CustomersProfileForm(forms.ModelForm):
     class Meta:
        model = Customer
        fields =['nombre','direccion','ciudad','móvil','provincia','codigo_postal']
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'direccion':forms.TextInput(attrs={'class':'form-control'}),
            'ciudad':forms.TextInput(attrs={'class' : 'form-control'}),
            'móvil' :forms. NumberInput(attrs={'class' : 'form-control'}),
            'provincia':forms.Select(attrs={'class' : 'form-control '}),
            'codigo_postal' :forms.NumberInput(attrs={'class' : ' form-control' }),
        }


                

