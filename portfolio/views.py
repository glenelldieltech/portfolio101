from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import threading 
from .models import ContactMessage 

# Home page - MALINIS NA VERSION
def index(request):
    return render(request, 'index.html')

# Contact form handler na may Database Saving at Background Email
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Siguradong naka-save ang mensahe sa Admin Panel
        ContactMessage.objects.create(
            name=name, email=email, subject=subject, message=message
        )

        # Background email process para iwas 500/502 errors sa Render
        full_message = f"Message from {name} ({email}):\n\n{message}"
        email_thread = threading.Thread(
            target=send_mail,
            args=(subject, full_message, settings.DEFAULT_FROM_EMAIL, ['glenelldieltech@gmail.com']),
            kwargs={'fail_silently': True}
        )
        email_thread.start()

        # Instant redirect sa homepage na may success message
        messages.success(request, "Thank you! Your message has been saved.")
        return redirect('/')
    return redirect('/')

# Iba pang views (Huwag galawin)
def portfolio_page(request):
    return render(request, 'portfolio.html')

def profile(request):
    return render(request, 'profile.html')

def profile2(request):
    return render(request, 'profile2.html')

def profile3(request):
    return render(request, 'roadmap.html')