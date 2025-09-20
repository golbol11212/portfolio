from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.

def midl_view(request):
    return render(request, 'midl.html')

def send_email_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if email and message:
            try:
                send_mail(
                    f'Сообщение с портфолио от {email}',
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.EMAIL_HOST_USER], # Отправляем на свой же адрес
                    fail_silently=False,
                )
                messages.success(request, 'Ваше сообщение успешно отправлено!')
            except Exception as e:
                messages.error(request, f'Произошла ошибка при отправке сообщения: {e}')
        else:
            messages.error(request, 'Пожалуйста, заполните все поля формы.')
            
    return redirect('midl')
