from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages



# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        number = request.POST['number']
        message = request.POST['message']


        email_subject = f'You have a new message from StudyPal regarding {subject}'
        message_body = f'Name: {name}\nEmail: {email}\nPhone: {number}\nMessage: {message}'

        try:
            admin_info = User.objects.get(is_superuser=True)
            admin_email = admin_info.email

            send_mail(
                email_subject,
                message_body,
                "futuresync101@gmail.com",
                [admin_email],
                fail_silently=False,
            )

            messages.success(request, 'Thank you for contacting us, we will get back to you shortly.')
        except User.DoesNotExist:
            messages.error(request, 'Admin user not found.')
        except Exception as e:
            messages.error(request, f'An error occurred: {e}')

        return redirect('contact')

    return render(request, 'pages/contact.html')


def about(request):
    return render(request, 'pages/about.html')


