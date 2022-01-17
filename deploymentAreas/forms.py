from django import forms
class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'style':'border-radius:10px; hover{border-color:red;}'}))
    password = forms.CharField(max_length=100, 
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'style':'border-radius:10px;'}))

class RegistrationForm(forms.Form):
    firstname = forms.CharField(label="First name", max_length=100,
                                widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                             'style':'border-radius:10px;'}))
    lastname = forms.CharField(label="Last name", max_length=100,
                               widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                             'style':'border-radius:10px;'}))
    email = forms.CharField(label="Email", max_length=100,
                            widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                             'style':'border-radius:10px;'}))
    username = forms.CharField(label="Username", max_length=100,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'style':'border-radius:10px;'}))
    password = forms.CharField(max_length=100, 
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'style':'border-radius:10px;'}))
    confirm_password = forms.CharField(max_length=100, 
                                       widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                 'style':'border-radius:10px;'}))