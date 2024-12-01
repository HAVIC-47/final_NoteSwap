from django import forms
from .models import PDFUpload
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
class PDFUploadForm(forms.ModelForm):
    class Meta:
        model = PDFUpload
        fields = ['pdf_file']

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignUpForm(UserCreationForm):
    USER_ROLES = [
        ('note_provider', 'Note Provider'),
        ('regular_user', 'Regular User'),
    ]
    user_role = forms.ChoiceField(choices=USER_ROLES, required=True, widget=forms.Select(attrs={
        'class': 'form-control',
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'user_role')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_role = self.cleaned_data['user_role']
        if commit:
            user.save()
        return user


from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import User

class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'occupation', 'university', 'department', 'gender']

from .models import Image
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields=("caption","image")