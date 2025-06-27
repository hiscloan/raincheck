from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactSubmission
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def home(request):
    return render(request, 'raincheck_app/home.html')

def services(request):
    return render(request, 'raincheck_app/services.html')

def about_us(request):
    return render(request, 'raincheck_app/about_us.html')

def contact(request):
    return render(request, 'raincheck_app/contact.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactSubmission.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                message=form.cleaned_data['message']
            )
            return redirect('contact')
  # Redirect to clear the form or to a success page
    else:
        form = ContactForm()

    return render(request, 'raincheck_app/contact.html', {'form': form})

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        email = request.POST.get('email')

        full_message = f"From: {name} <{email}>\n\n{message}"

        send_mail(
            subject='New Contact Form Submission',
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['rainalexiss@gmail.com'],
            fail_silently=False,
        )