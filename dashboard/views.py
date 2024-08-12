from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
import os
import PyPDF2

@login_required(login_url='login')
def user_contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        number = request.POST['number']
        message = request.POST['message']


        email_subject = f'You have a new message from StudyPal regarding {subject}. (Existing User)'
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

        return redirect('user_contact')

    return render(request, "dashboard/user_contact.html")


@login_required(login_url='login')
def user_profile(request):
    if request.method == "POST":
        user = request.user
        # Update profile information
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        if username:
            user.username = username
        if email:
            user.email = email
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        user.save()
        messages.success(request, 'Your profile has been updated.')
        return redirect('user_profile')

    return render(request, 'dashboard/user_profile.html')

def change_password(request):
    if request.method == "POST":
        user = request.user
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if old_password and new_password and confirm_password:
            if new_password == confirm_password:
                if user.check_password(old_password):
                    user.set_password(new_password)
                    user.save()
                    update_session_auth_hash(request, user)  # Important to keep the user logged in
                    messages.success(request, 'Your password has been updated.')
                else:
                    messages.error(request, 'Old password is incorrect.')
            else:
                messages.error(request, 'New passwords do not match.')
        return redirect('user_profile')


def extract_text_from_pdf(pdf_file):
    with pdf_file.open('rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

@csrf_exempt
def pdf_data(request):
    if request.method == 'POST' and 'file' in request.FILES:
        file = request.FILES['file']
        file_path = default_storage.save('temp.pdf', file)
        temp_pdf_path = default_storage.path(file_path)

        pdf_text = extract_text_from_pdf(file)  # Use the file object directly
        default_storage.delete(file_path)  # Clean up the temporary file

        return JsonResponse({'text': pdf_text})

    return JsonResponse({'error': 'Invalid request'}, status=400)


@login_required(login_url='login')
def user_dashboard(request):
    return render(request, 'dashboard/user_dashboard.html')

