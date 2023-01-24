"""
To render html web pages
"""
from django.http import HttpResponse
import random 


def home_view(request):
    """
    Take in a request (Django sends request)
    Return HTML as a responce (we pick to return the response)
    """
    name = "Swamy"
    number = random.randint(10, 12321)
    HTML_STRING = f"""
    <h1>Hello {name} - {number}</h1>
    """
    return HttpResponse(HTML_STRING)