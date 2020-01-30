from django import forms
from .models import Bug, Image
from django.utils import timezone
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from .custom_layout_object import *

class BugForm(forms.ModelForm):
    class Meta:
        model= Bug
        exclude =[
            'bug_states',
            'pub_date',
            'reported_by'
            ]
    def __init__(self, *args, **kwargs):
        super(BugForm,self).__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'

        self.helper.layout = Layout(
            Div(
                Field('bug_title'),
                Field('bug_description', css_class = 'row-fluid' ),
                Fieldset('Add Image',
                    Formset('image')),
                # Field('note'),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'save')),
                ButtonHolder(Submit('cancel', 'Cancel', css_class='btn-danger',formnovalidate='formnovalidate'))
                )
        )

class ImageForm(forms.ModelForm):
    image =  forms.ImageField(label='Image')
    class Meta:
        model= Image
        fields = ('image',)

ImageFormSet = inlineformset_factory(
    Bug, Image, form=ImageForm, fields=['image'], extra=1, can_delete=True, max_num=3, validate_max=True
)
