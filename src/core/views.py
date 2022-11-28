from django.shortcuts import render
fron django.http import HttpResponse

# Create your views here.
def home(request):
  HttpResponse("<h2>Welcome to the Social Media platform</h2>")
