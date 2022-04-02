from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	return HttpResponse("Hello World!")
def page1(requenst):
    my_dict = {'insert_me' : 'hello Im from views.py'}
    return render(requenst, 'first_app/index.html', context=my_dict)

# Create your views here.
