from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index_adopcion(request):
	return HttpResponse("I'm the principal page of the adoption's apps xD")