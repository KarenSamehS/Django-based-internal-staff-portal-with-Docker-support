
from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["department", "bio", "avatar"]
        widgets = {
            "department": forms.TextInput(
                attrs={"class": "validate"}
            ),
            "bio": forms.Textarea(
                attrs={"class": "materialize-textarea"}
            ),
        }
