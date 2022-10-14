from dataclasses import field
import email
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import Questions,Score

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = "__all__"
    question = forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'class':'form-control form-control-lg',
				   'id':'form3Example1cg'}))
    option_1= forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'class':'form-control form-control-lg',
				   'id':'form3Example1cg'}))
    option_2= forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'class':'form-control form-control-lg',
				   'id':'form3Example1cg'}))
    option_3= forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'class':'form-control form-control-lg',
				   'id':'form3Example1cg'}))
    option_4= forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'class':'form-control form-control-lg',
				   'id':'form3Example1cg'}))
    answer= forms.ChoiceField(
                                widget=forms.Select
                                (attrs={'class':'form-control form-control-lg',
				   'id':'form3Example1cg'}) , choices=[('option_1','option_1'),('option_2','option_2'),('option_3','option_3'),('option_4','option_4'),]                         
                           )

class SignUpForm(UserCreationForm):
    
    username = forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'class':'form-control form-control-lg',
				   'id':'form3Example1cg'}))
    
    email = forms.CharField(max_length=100,
                           widget= forms.EmailInput
                           (attrs={'class':'form-control form-control-lg',
				   'id':'form3Example1cg'}))
    
    first_name = forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'class':'form-control form-control-lg',
				   'id':'form3Example1cg'}))
    
    last_name = forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'class':'form-control form-control-lg',
				   'id':'form3Example1cg'}))
    
    

    password1 = forms.CharField(max_length=100,
                           widget= forms.PasswordInput
                           (attrs={'class':'form-control form-control-lg',
				   'id':'form3Example1cg'}))
    
    password2 = forms.CharField(max_length=100,
                           widget= forms.PasswordInput
                           (attrs={'class':'form-control form-control-lg',
				   'id':'form3Example1cg'}))

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password1','password2')


class LogInForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'class':'form-control form-control-lg',
				   'id':'form3Example1cg'}))
    
    password = forms.CharField(max_length=100,
                           widget= forms.PasswordInput
                           (attrs={'class':'form-control form-control-lg',
				   'id':'form3Example1cg'}))
    