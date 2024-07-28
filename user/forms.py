from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length= 150)
    password = forms.CharField(widget= forms.PasswordInput)
    password_confirm= forms.CharField(widget=forms.PasswordInput)


    def clean(self):
        password = self.cleaned_data['password']
        password_confirm = self.cleaned_data['password_confirm']
        if password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают')
        return self.cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget = forms.PasswordInput)