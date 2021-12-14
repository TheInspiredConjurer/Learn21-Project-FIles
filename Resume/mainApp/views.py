from django.shortcuts import render, redirect
from django.urls import reverse

from .models import ContactUs
from .forms import ContactUsForm

# Create your views here.

def index(request):
    if(request.method == 'POST'):
        cu = ContactUsForm(request.POST)
        if cu.is_valid():
            obj = ContactUs()
            obj.name = cu.cleaned_data['name']
            obj.email = cu.cleaned_data['email']
            obj.subject = cu.cleaned_data['subject']
            obj.message = cu.cleaned_data['message']
            obj.save()
            return redirect(reverse('success'))
            

    else:
        cu = ContactUsForm()
        return render(request, 'index.html')


def portfoliodetails(request):
    return render(request, 'portfolio-details.html')

def success(request):
    return render(request, 'success.html')

