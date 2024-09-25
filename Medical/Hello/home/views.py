from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from django.contrib import messages
from home.models import Contact

# Create your views here.
def index(request):
    return render(request, "index.html")
    # return HttpResponse("This is a homepage")

def about(request):
    return HttpResponse("This is a about page")

def services(request):
    return HttpResponse("This is a service page")

def contact(request):
    if request.method == 'POST':
        # Handle the form submission here
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # You can process and store the data here
        contact = Contact(name=name, email=email, message=message, date = datetime.today())
        contact.save()
        return redirect('home')  # Ensure 'home' is the name of your index page URL
    return render(request, 'index.html')
