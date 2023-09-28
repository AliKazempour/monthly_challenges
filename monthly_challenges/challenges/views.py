from django.http import (HttpResponse, HttpResponseNotFound,
                         HttpResponseRedirect)
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "Go to university very early ",
    "february": "Playing video game every day",
    "march": "Reading a Book",
    "april": "Learn a New Skill Challenge",
    "may": "30-Day Digital Detox Challenge",
    "june": "30-Day Fitness Challenge",
    "july": "Random Acts of Kindness Challenge",
    "august":  "Journaling Challenge",
    "september":  "Photography Challenge",
    "october": "30-Day Meditation Challenge",
    "november": "Gratitude Challenge",
    "december": "The Giving Challenge"
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)
    
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months) or month < 1:
        return HttpResponseNotFound("Invalid month!")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge",args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def month_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,"challenges/challenge.html",{
            "text":challenge_text,
            "month_name":month.capitalize()
        })
    except:
        return HttpResponseNotFound("<h1>This month is not exist!</h1>")
