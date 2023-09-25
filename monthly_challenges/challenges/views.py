from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

def month_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Go to university very early "
    elif month == "february":
        challenge_text = "Playing video game every day"
    elif month == "march":
        challenge_text = "Reading a Book"
    else:
        return HttpResponseNotFound("This month is not exist!")
    return HttpResponse(challenge_text)
