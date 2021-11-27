from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("index.html")

def login(request):
    return HttpResponse("login.html")

def aboutus(request):
    return HttpResponse("about-us.html")