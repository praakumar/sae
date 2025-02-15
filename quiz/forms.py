from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
	email=forms.EmailField(required=True)

	class Meta:
		model=User
		fields=(
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2',)

		def save(self,commit='True'):
			user=super(RegistrationForm,self).save(commit=False)
			user.first_name=self.cleaned_data['first_name']
			user.last_name=self.cleaned_data['last_name']
			user.email=self.cleaned_data['email']

			if commit:
				user.save()
			return user
class LoginForm(forms.Form):
	username=forms.CharField(label='User Name',max_length=100)
	password=forms.CharField(label='password',max_length=100)
	