from django.shortcuts import render, redirect # Siguraduhing may 'redirect' dito
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Home page
def index(request):
    return render(request, 'index.html')

# ITO YUNG IPAPALIT MO (Paste it here)
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = f"Message from {name} ({email}):\n\n{message}"

        try:
            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                ['glenelldieltech@gmail.com'],
                fail_silently=True, 
            )
            messages.success(request, "Your message has been sent successfully!")
        except Exception:
            messages.error(request, "There was an issue, but we will get back to you.")
        
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