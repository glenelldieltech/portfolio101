from django.shortcuts import render, redirect # Siguraduhing may redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Home page
def index(request):
    return render(request, 'index.html')

# Contact form handler - ITO ANG PINALITAN NATIN
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
                settings.DEFAULT_FROM_EMAIL,  # sender
                ['glenelldieltech@gmail.com'], # receiver
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            # Dito natin makikita kung ano ang error sa Gmail sa mismong website
            messages.error(request, f"Error sending message: {e}")
            return redirect('portfolio:index')

        # Gagamit tayo ng redirect imbes na render para iwas error sa live
        return redirect('portfolio:index')

    return redirect('portfolio:index')

# Portfolio page at iba pa... (mananatiling pareho)
def portfolio_page(request):
    return render(request, 'portfolio.html')

def profile(request):
    return render(request, 'profile.html')

def profile2(request):
    return render(request, 'profile2.html')

def profile3(request):
    return render(request, 'roadmap.html')