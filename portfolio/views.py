from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import threading # Importante ito para sa background task

# Home page
def index(request):
    return render(request, 'index.html')

# FINAL FIX: Gagamit ng threading para iwas Internal Server Error
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = f"Message from {name} ({email}):\n\n{message}"

        # Dito natin gagawin ang background task
        # Hindi na maghihintay ang website mo kung mag-sa-success o fail ang email
        email_thread = threading.Thread(
            target=send_mail,
            args=(subject, full_message, settings.DEFAULT_FROM_EMAIL, ['glenelldieltech@gmail.com']),
            kwargs={'fail_silently': True}
        )
        email_thread.start()

        # Agad na mag-re-redirect para hindi mag-timeout ang Render/Cloudflare
        messages.success(request, "Thank you! Your message is being processed.")
        return redirect('/') 

    return redirect('/')

# Panatilihin ang iyong ibang views sa ibaba
def portfolio_page(request):
    return render(request, 'portfolio.html')

def profile(request):
    return render(request, 'profile.html')

def profile2(request):
    return render(request, 'profile2.html')

def profile3(request):
    return render(request, 'roadmap.html')