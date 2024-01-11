from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import NewUSerRegisterForm
from django.contrib.auth import login
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.hashers import make_password

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = NewUSerRegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            remember_password = form.cleaned_data.get('password1')
            user.password = make_password(form.cleaned_data.get('password1'),hasher='md5')
            user.save()
            try:           
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')     
                messages.success(request, "User registration successful.")
                mail_subject = "Registration in Payment List Application "
                message = "The registration was successful and this is your Username: %s and your password: %s" % (
                    user.username, remember_password)
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(mail_subject, message,
                        settings.DEFAULT_FROM_EMAIL, [to_email])           
                email.send(fail_silently=False)              
            except:
                print("The SMTP server is not working.")
            return redirect('home:home_all')
        messages.error(request, "User registration failed.")
    form = NewUSerRegisterForm()
    return render(request, 'register.html', {'form':form})        