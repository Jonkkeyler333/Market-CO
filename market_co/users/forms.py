from django import forms
from .models import CustomUser

class Register_form(forms.ModelForm):
    password1=forms.CharField(widget=forms.PasswordInput,label="Contraseña")
    password2=forms.CharField(widget=forms.PasswordInput,label="Confirmar contraseña")
    class Meta:
        model=CustomUser
        fields=['username','email','role']
    
    def clean_password2(self):
        password1=self.cleaned_data.get("password1")
        password2=self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2

    def save(self,commit=True):
        user=super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
class Login_form(forms.ModelForm):
    username=forms.CharField(max_length=150,label="Nombre de usuario",required=True)
    password=forms.CharField(widget=forms.PasswordInput,label="Contraseña",required=True)