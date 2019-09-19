from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


def portfolio(request):
    return render(request, "portfolio.html")

def resume(request):
    return render(request, "resume.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = 'Email From Portfolio App'
            message = 'Email from {} with email {} \nDetails: \n{}'.format(
                                                    cd['Name'], cd['Email'], cd['Message'])
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['hunter.me33@gmail.com',]
            send_mail(subject, message, email_from, recipient_list)
            messages.success(request, 'Email sent Successfully')
            return redirect('contact')
    form = ContactForm()
    return render(request, "ContactForm.html", {'form':form})
