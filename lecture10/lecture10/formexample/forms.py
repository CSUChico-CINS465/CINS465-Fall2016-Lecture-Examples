from django import forms

from django.core.validators import validate_slug

class SubmissionForm(forms.Form):
    submission = forms.CharField(
        max_length=144,
        validators=[validate_slug],
        label='Suggest Topic',
        required=True,
        help_text='144 characters max',
        widget=forms.TextInput(attrs={'size':'50', 'placeholder':"large-4.columns"}))
