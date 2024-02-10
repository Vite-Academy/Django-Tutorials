from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import * 
    
# creating a form   

# class InputForm(forms.Form):  
#     first_name = forms.CharField(max_length = 200)  
#     last_name = forms.CharField(max_length = 200)  
#     roll_number = forms.IntegerField(  
#                      help_text = "Enter 6 digit roll number"
#                      )  
#     password = forms.CharField(widget = forms.PasswordInput())


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        # fields = ('title', 'text',)
        fields = "__all__"