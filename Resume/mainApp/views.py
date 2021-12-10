from django.shortcuts import render, HttpResponseRedirect

# Create your views here.

def index(request):
    if(request.method == 'POST'):
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        return render(request, 'index.html')

    else:
        return render(request, 'index.html')



def portfoliodetails(request):
    return render(request, 'portfolio-details.html')
