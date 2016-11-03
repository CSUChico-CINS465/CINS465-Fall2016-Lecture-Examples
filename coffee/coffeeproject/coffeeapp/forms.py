from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Blog

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'})
    )
    password = forms.CharField(
        label="Password",
        max_length=32,
        widget=forms.PasswordInput()
    )

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email", required=True)

    class Meta:
        model = User
        fields= ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user=super(RegisterForm,self).save(commit=False)
        user.email=self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class blog_entry(forms.Form):
    title=forms.CharField(label="Title",max_length=144)
    content=forms.CharField(label="Blog Content",widget=forms.Textarea)
    image=forms.ImageField(label="Image File")
    image_description=forms.CharField(label="Image Description", max_length=144)

    def save(self, request , commit=True):
        blog = Blog()
        blog.title=self.cleaned_data['title']
        blog.content=self.cleaned_data['content']
        blog.image=self.cleaned_data['image']
        blog.image_description=self.cleaned_data['image_description']
        blog.author=request.user
        if commit:
            blog.save()
        return blog
