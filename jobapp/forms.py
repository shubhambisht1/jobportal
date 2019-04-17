from django import forms
from jobapp.models import signup,feedback
class signupForm(forms.ModelForm):
    class Meta:
        model=signup
        fields='__all__'
class feedbackForm(forms.ModelForm):
    class Meta:
        model=feedback
        fields='__all__'
