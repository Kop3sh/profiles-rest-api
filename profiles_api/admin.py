from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import UserProfile


# class AddUserForm(forms.ModelForm):
#     """
#     New User Form. Requires password confirmation.
#     """
#     password1 = forms.CharField(
#         label='Password', widget=forms.PasswordInput
#     )
#     password2 = forms.CharField(
#         label='Confirm password', widget=forms.PasswordInput
#     )

#     class Meta:
#         model = UserProfile
#         fields = ('email', 'name')

#     def clean_password2(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords do not match")
#         return password2

#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user


# class UpdateUserForm(forms.ModelForm):
#     """
#     Update User Form. Doesn't allow changing password in the Admin.
#     """
#     password = ReadOnlyPasswordHashField()

#     class Meta:
#         model = UserProfile
#         fields = (
#             'email', 'password', 'name', 'is_active',
#             'is_staff'
#         )

#     def clean_password(self):
#         # Password can't be changed in the admin
#         return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # form = UpdateUserForm
    # add_form = AddUserForm

    list_display = ('email', 'name', 'is_staff')
    list_filter = ('is_staff', )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email', 'name', 'password1',
                    'password2'
                )
            }
        ),
    )
    search_fields = ('email', 'name')
    ordering = ('email', 'name')
    filter_horizontal = ()



admin.site.register(UserProfile)