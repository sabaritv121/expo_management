from django import forms
from django.contrib.auth.forms import UserCreationForm

from Expo_app.models import Login_view, users, Company, CreateExpo


class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)

    class Meta:
        model = Login_view
        fields = ('username','password1','password2',)


class UsersRegister(forms.ModelForm):

    class Meta:
        model = users
        fields = "__all__"
        exclude = ("user",)



class DateInput(forms.DateInput):
    input_type = 'date'

class CompanyRegister(forms.ModelForm):

    class Meta:
        model = Company
        fields = "__all__"
        exclude = ("user","status")


class ExpoForm(forms.ModelForm):
    start_date = forms.DateField(widget=DateInput)
    end_date = forms.DateField(widget=DateInput)


    class Meta:
        model = CreateExpo
        fields = '__all__'