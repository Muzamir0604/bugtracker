# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from django.contrib.auth.admin import UserAdmin

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name', 'email','contact','address', 'postal')

    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        del self.fields['password']
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('username'),
                Div(
                    Div(Field('first_name'),css_class='col-md-6'),
                    Div(Field('last_name'),css_class='col-md-6'),
                    css_class='row'),
                Field('email'),
                Field('contact'),
                Field('address'),
                Field('postal'),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'save')),
                ButtonHolder(Submit('cancel', 'Cancel', css_class='btn-danger',formnovalidate='formnovalidate'))
                )
        )

class CustomUserCreateAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    prepopulated_fields = {'username':('first_name','last_name',)}

    add_fieldsets=(
     (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'password1', 'password2', ),
        }),
    )
