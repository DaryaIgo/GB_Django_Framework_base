from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse


def send_verify_mail(user):
    verify_link = reverse("auth:verify", args=[user.email, user.activation_key])

    title = f'Подтверждение учетной записи {user.username}'

    message = f'" Для подтверждения {user.username}' \
              f'на партале {settings.DOMAIN_NAME} перейдите по ссылке:' \
              f'{settings.DOMAIN_NAME}{verify_link}"'

    return send_mail(
        title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False
    )
