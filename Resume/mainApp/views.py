from django.shortcuts import render
from .forms import ContactForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def portfoliodetails(request):
    return render(request, 'portfolio-details.html')
