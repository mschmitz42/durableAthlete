from django import forms
from .models import Program


class ContactForm(forms.Form):
    name = forms.CharField(required=True,
                           label="Name",
                           error_messages={"required": "Please enter your name"})
    email = forms.CharField(required=True,
                            label="Email",
                            error_messages={"required": "Please enter your Email Address"})
    subject = forms.CharField(required=True,
                              label="Subject",
                              error_messages={"required": "Please enter a subject"})
    message = forms.CharField(widget=forms.Textarea,
                              label="Message",
                              error_messages={"required": "Please enter a message"})


class ProgramChoice(forms.Form):
    choices = Program.objects.filter(active=True).order_by('display_order').values_list('id', 'description')
    account_choices = (
        ("a1", "I need to create my Durability Builder account"),
        ("a2", "I have a Durability Builder account"),
    )
    program = forms.ChoiceField(label='',
                                choices=choices)

    account = forms.ChoiceField(label='',
                                choices=account_choices,
                                widget=forms.RadioSelect(attrs={'class': "program_select_item"}))

