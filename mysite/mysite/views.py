# created by me

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':'shreyash', 'place':'earth'}
    return render(request, 'index.html',params)
    # render takes 3 args

def home(request):
    return HttpResponse("Home")


def about(request):
    return HttpResponse("hello there <a href='/'>back</a>") #through this it will go back to default link which is 127.0.0.1:8000 (i.e. home page)

def open_google(request):
    return HttpResponse('''<a href="https://www.google.com/">Click here</a> <br>
                        <a href="http://127.0.0.1:8000/about">back to about page</a>''')
    
