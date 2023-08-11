from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Enter password',
        'class' : 'form-control',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Confirm password'
    }))
    class Meta:
        model = Account
        fields = [ 'first_name','last_name','email','password','phone_number']

    def __init__(self,*args,**kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] ='Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] ='Enter Last Name'
        self.fields['phone_number'].widget.attrs['placeholder'] ='Enter phone number'
        self.fields['email'].widget.attrs['placeholder'] ='Enter email address'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] ='form-control'