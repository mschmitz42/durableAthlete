from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .forms import ContactForm, ProgramChoice
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect


def durabilitybuilder_index(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            body = {
                "name": "Name: " + form.cleaned_data["name"],
                "email": "Email Address: " + form.cleaned_data["email"],
                "subject": "Subject: " + form.cleaned_data["subject"],
                "message": "Message: " + form.cleaned_data["message"],
            }
            message = "\n".join(body.values())
            try:
                send_mail("Message From Durability Builder Website",
                          message,
                          "mike@durabilitybuilder.com",
                          ["mikeschmitz42@gmail.com", "Tim@MultisportEnduranceAcademy.com"])
            except BadHeaderError:
                return HttpResponse("Invalid Header Found")

            return redirect("durabilityBuilder:send_confirm")

    return render(request, 'durabilityBuilder/index.html', {"form": form})


def under_construction(request):

    return render(request, 'durabilityBuilder/under_construction.html')


def send_confirmation(request):

    return render(request, 'durabilityBuilder/send_confirmation.html')


def get_started(request):
    if request.method == "GET":
        form = ProgramChoice()
    else:
        form = ProgramChoice(request.POST)
        if form.is_valid():
            program_choice = form.cleaned_data["program"]
            account = form.cleaned_data["account"]

            request.session["program_choice"] = program_choice

            if account == "a1":
                return redirect("durabilityBuilder:under_construction")
            else:
                return redirect("durabilityBuilder:dashboard")

        else:
            return HttpResponse("Invalid Form Value(s)")

    return render(request, 'durabilityBuilder/get_started.html', {"form": form})


def user_is_staff(user):
    return user.is_staff


@login_required
def dashboard(request):
    return render(request, 'durabilityBuilder/dashboard.html')


@login_required
def intro_day1(request):
    return render(request, 'durabilityBuilder/intro_day1.html')


@login_required
def intro_day2(request):
    return render(request, 'durabilityBuilder/intro_day2.html')


@login_required
def intro_day3(request):
    return render(request, 'durabilityBuilder/intro_day3.html')


@login_required
def intro_day4(request):
    return render(request, 'durabilityBuilder/intro_day4.html')


@login_required
def intro_day5(request):
    return render(request, 'durabilityBuilder/intro_day5.html')


@login_required
def intro_day6(request):
    return render(request, 'durabilityBuilder/intro_day6.html')


@login_required
def intro_day7(request):
    return render(request, 'durabilityBuilder/intro_day7.html')


@login_required
def intro_day8(request):
    return render(request, 'durabilityBuilder/intro_day8.html')


@login_required
def intro_day9(request):
    return render(request, 'durabilityBuilder/intro_day9.html')


@login_required
def intro_day10(request):
    return render(request, 'durabilityBuilder/intro_day10.html')


@login_required
def intro_day11(request):
    return render(request, 'durabilityBuilder/intro_day11.html')


@login_required
def intro_day12(request):
    return render(request, 'durabilityBuilder/intro_day12.html')


@login_required
def intro_day13(request):
    return render(request, 'durabilityBuilder/intro_day13.html')


@login_required
def intro_day14(request):
    return render(request, 'durabilityBuilder/intro_day14.html')


