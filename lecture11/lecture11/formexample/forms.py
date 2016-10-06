from django import forms

from django.core.validators import validate_slug

def verify_suggestion(value):
    if not len(value)>5:
        raise forms.ValidationError("Suggestion must be longer than 5 characters")
    if not value[0]=='b':
        raise forms.ValidationError("Suggestion must start with letter 'b'")
    return value

class SubmissionForm(forms.Form):
    submission = forms.CharField(
        max_length=144,
        validators=[validate_slug],
        label='Suggest Topic',
        required=True,
        help_text='144 characters max',
        widget=forms.TextInput(attrs={'size':'50', 'class':"large-8.columns"}))
