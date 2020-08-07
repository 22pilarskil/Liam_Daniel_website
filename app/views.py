from django.shortcuts import render
from django.http import HttpResponse

def homeview(request):
	html = "<p>Hello World</p>"
	#return render(request, "homepage.html")
	return HttpResponse(html)

# Create your views here.
