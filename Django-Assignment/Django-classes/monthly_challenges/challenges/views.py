from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Dictionary of monthly challenges
monthly_challenge_dict = {
    'january': 'This is new year!',
    'february': 'Walk for at least 20 minutes every day!',
    'march': 'Learn Django for at least 20 minutes every day!',
    'april': 'Learn Python for at least 10 hours every day!',
    'may': 'Run for at least 5 km every day!',
    'june': 'Read a book every week!',
    'july': 'Practice coding every day!',
    'august': 'Meditate for at least 20 minutes every day!',
    'september': 'Write a journal every day!',
    'october': 'Learn a new skill every month!',
    'november': 'Volunteer for a good cause!',
    'december': 'Reflect on the year and plan for the next!'
}

def index(request):
    # List all the months as links
    list_items = ""
    months = list(monthly_challenge_dict.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("monthly-challenge", args=[month])
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenge_dict.keys())

    if month > len(months) or month < 1:
        return HttpResponseNotFound('Invalid month')

    redirect_month = months[month - 1]
    redirect_path = reverse("monthly-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenge_dict[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except KeyError:
        return HttpResponseNotFound('<h1>Month not found</h1>')
