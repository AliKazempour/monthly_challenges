from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

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


def month_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not exist!")
