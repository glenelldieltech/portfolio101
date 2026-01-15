import os
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import threading 
from .models import ContactMessage 

def index(request):
    # Tinanggal na natin ang User logic dito para hindi na mag-check sa database bawat load
    return render(request, 'index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Pag-save sa database
        ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)
        
        # Pag-send ng email sa background gamit ang threading
        full_message = f"Message from {name} ({email}):\n\n{message}"
        email_thread = threading.Thread(
            target=send_mail, 
            args=(subject, full_message, settings.DEFAULT_FROM_EMAIL, ['glenelldieltech@gmail.com']), 
            kwargs={'fail_silently': True}
        )
        email_thread.start()
        
        messages.success(request, "Thank you! Your message has been saved.")
        return redirect('/')
    return redirect('/')

def portfolio_page(request): return render(request, 'portfolio.html')
def profile(request): return render(request, 'profile.html')
def profile2(request): return render(request, 'profile2.html')
def profile3(request): return render(request, 'roadmap.html')