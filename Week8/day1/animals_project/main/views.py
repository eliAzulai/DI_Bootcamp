from django.shortcuts import render
from datetime import datetime

# Create your views here.

def homepage(request):
    name_is = 'toby'
    today = datetime.now()
    return render(request, 'homepage.html', 
                  {'now' : today, 'name_is':'Toby', 'letters': list('abcdefg')})


def about(request, my_name):
    return render(request, 'about.html', {'name': my_name})