# created by me

import string
from django.http import HttpResponse
from django.shortcuts import render
from string import punctuation


def index(request):
    
    return render(request, 'index.html')
    # render takes 3 args third argument is parameters

def home(request):
    return HttpResponse("Home")


def about(request):
    return HttpResponse("hello there <a href='/'>back</a>") #through this it will go back to default link which is 127.0.0.1:8000 (i.e. home page)

def open_google(request):
    return HttpResponse('''<a href="https://www.google.com/">Click here</a> <br>
                        <a href="http://127.0.0.1:8000/about">back to about page</a>''')
    

def removepunc(request):
    # getting the data (text) from the form
    
    # here also we will be using post method
    djtext = request.POST.get('text','default')
    
    #check checkbox values setting it to off by default
    rmpunc = request.POST.get('removepunc','off')
    
    fullcaps = request.POST.get('fullcaps','off')
    
    charcount = request.POST.get('charcount','off')
    
    
    # print(rmpunc)
    # print(type(djtext))

    
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    
    analyzed=""

    
    # check which checkbox is on
    if rmpunc=='on':
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        
        params = {'analyzed_text': analyzed}
        
        return render(request,'analyze.html',params)
    
    elif fullcaps=='on':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
            
        params = {'analyzed_text': analyzed}
        
        return render(request,'analyze.html',params)
    
    elif charcount=='on':
        length=0
        for char in djtext:
            if char == " ":
                pass
            else:
                length=length+1
                
       
        params = {'analyzed_text':  length}
        
        return render(request,'analyze.html',params)
        
    else:
        return HttpResponse("Error")
