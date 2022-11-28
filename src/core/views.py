from django.shortcuts import render
fron django.http import HttpResponse

# Create your views here.
def index(request):
  HttpResponse("Hello, Welcome to the index page")

def home(request):
  HttpResponse("<h2>Welcome to the Social Media platform</h2>")
