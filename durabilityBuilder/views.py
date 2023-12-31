from django.shortcuts import render

# Create your views here.


def durabilityBuilder_index(request):

    return render(request, 'durabilityBuilder/index.html')
