from django import forms
from User.models import Worker, UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'password', 'email')

class WorkerForm(forms.ModelForm):
    class Meta():
        model = Worker
        fields = ('first_name', 'last_name', 'phone', 'basic_charge', 'work')
        
class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('first_name', 'last_name', 'phone', 'address')
