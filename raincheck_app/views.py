from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactSubmission


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