from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name',
            'email': 'Email'
        }

    # adding some styles to the form to make sure all fields are styled
    # embedding a class named input. You can add other relevant directives this way
    # self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'Add Title'})
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

# class ProfileForm(ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['name', 'email', 'username', 'location', 'bio',
#                     'short_intro', 'profile_image', 'social_github',
#                     'social_linkedin', 'social_youtube'
#                 ]

#     # adding some styles to the form to make sure all fields are styled
#     # embedding a class named input. You can add other relevant directives this way
#     # self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'Add Title'})
#     def __init__(self, *args, **kwargs):
#         super(ProfileForm, self).__init__(*args, **kwargs)

#         for name, field in self.fields.items():
#             field.widget.attrs.update({'class': 'input'})