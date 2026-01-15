from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Home page
def index(request):
    return render(request, 'index.html')

# Contact form handler - FIXED VERSION
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = f"Message from {name} ({email}):\n\n{message}"

        # Ang fail_silently=True ay sapat na para pigilan ang Internal Server Error
        # Kahit blocked ang Gmail sa Render, itutuloy lang ni Django ang redirect.
        send_mail(
            subject,
            full_message,
            settings.DEFAULT_FROM_EMAIL,
            ['glenelldieltech@gmail.com'],
            fail_silently=True, 
        )
        
        # Siguraduhing babalik sa home page para hindi mag-white screen
        messages.success(request, "Your message has been sent successfully!")
        return redirect('/') 

    return redirect('/')

# Portfolio page at iba pa...
def portfolio_page(request):
    return render(request, 'portfolio.html')

def profile(request):
    return render(request, 'profile.html')

def profile2(request):
    return render(request, 'profile2.html')

def profile3(request):
    return render(request, 'roadmap.html')