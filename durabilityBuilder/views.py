from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect


def durabilityBuilder_index(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            body = {
                "name": form.cleaned_data["name"],
                "email": form.cleaned_data["email"],
                "subject": form.cleaned_data["subject"],
                "message": form.cleaned_data["message"],
            }
            message = "\n".join(body.values())
            try:
                send_mail("Message From Durability Builder Website",
                          message,
                          "mike@durabilitybuilder.com",
                          ["mikeschmitz42@icloud.com"])
            except BadHeaderError:
                return HttpResponse("Invalid Header Found")

            return redirect("durabilityBuilder:send_confirm")

    return render(request, 'durabilityBuilder/index.html', {"form": form})


def send_confirmation(request):

    return render(request, 'durabilityBuilder/send_confirmation.html')


def get_started(request):

    return render(request, 'durabilityBuilder/get_started.html')
