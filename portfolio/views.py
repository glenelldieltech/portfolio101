from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Home page
def index(request):
    return render(request, 'index.html')

# Contact form handler
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
                ['glendiel09@gmail.com'],     # receiver
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, f"Error sending message: {e}")

        # Render the same index page with scroll flag
        return render(request, 'index.html', {'scroll_to_contact': True})

    # kung GET request, diretso rin sa homepage
    return render(request, 'index.html')


# Portfolio page
def portfolio_page(request):
    return render(request, 'portfolio.html')

# Profile page
def profile(request):
    return render(request, 'profile.html')

def profile2(request):
    return render(request, 'profile2.html')

def profile3(request):
    return render(request, 'roadmap.html')