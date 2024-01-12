from django import forms


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

