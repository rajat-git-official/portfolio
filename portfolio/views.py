from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

def home(request):
    return render(request, 'portfolio/home.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Handle form submission, for example, send an email
        send_mail(
            f"Message from {name}",
            message,
            email,
            ['your-email@example.com'],
            fail_silently=False,
        )
        
        return HttpResponse('Thank you for your message.')
    return HttpResponse('Please submit the form.')
