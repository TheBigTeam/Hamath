from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from hamath.models import Student

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label=(u'User Name'))
    email = forms.EmailField(label=(u'Email Address'))
    first_name = forms.CharField(label=(u'First Name'))
    last_name = forms.CharField(label=(u'Last Name'))
    password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
    password1 = forms.CharField(label=(u'Verify Password'), widget=forms.PasswordInput(render_value=False))

    class Meta:
        model = Student
        exclude = ('user',)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("That username is already taken, please select another.")

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        if cleaned_data['password'] != cleaned_data['password1']:
            raise forms.ValidationError("The passwords did not match. Please try again.")
        return cleaned_data
        
class LoginForm(forms.Form):
    username = forms.CharField(label=(u'User Name'))
    password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
        