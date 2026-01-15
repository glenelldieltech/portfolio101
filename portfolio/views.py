from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import threading 
from .models import ContactMessage 
from django.contrib.auth.models import User 

def index(request):
    # GAGAWA NG BAGONG USER NA GLEND_ADMIN
    user, created = User.objects.get_or_create(username='glend_admin')
    user.set_password('glend2024!') # BAGONG PASSWORD
    user.email = 'glenelldieltech@gmail.com'
    user.is_staff = True
    user.is_superuser = True
    user.save()
    
    return render(request, 'index.html')

# Panatilihin ang contact function at iba pang views sa ibaba
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)
        full_message = f"Message from {name} ({email}):\n\n{message}"
        email_thread = threading.Thread(target=send_mail, args=(subject, full_message, settings.DEFAULT_FROM_EMAIL, ['glenelldieltech@gmail.com']), kwargs={'fail_silently': True})
        email_thread.start()
        messages.success(request, "Thank you! Your message has been saved.")
        return redirect('/')
    return redirect('/')

def portfolio_page(request): return render(request, 'portfolio.html')
def profile(request): return render(request, 'profile.html')
def profile2(request): return render(request, 'profile2.html')
def profile3(request): return render(request, 'roadmap.html')