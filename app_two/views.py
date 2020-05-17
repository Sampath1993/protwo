from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict = { 'second_insert_here': "I am Sampy" }
    return render(request, 'app_two/index.html', context=my_dict)