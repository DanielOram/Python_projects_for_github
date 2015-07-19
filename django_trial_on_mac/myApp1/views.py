from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
#from myApp1.models import sendEmail
# Create your views here.

#home page view
def index(request):
    return render(request, 'index.html')

#second page view
def confirmation_sent(request):
    text = 'Here is some text generated in python!' #this string is accessed by the html
    #confirmation = sendEmail.send(sendEmail)
    return render(request, 'confirmation_sent.html', {'text': text} )

