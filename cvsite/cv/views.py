from django.shortcuts import render
from .models import Profile


def accept(request):
    return render(request, "cv/accept.html")
