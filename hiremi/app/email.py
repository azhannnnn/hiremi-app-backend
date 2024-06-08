from django.core.mail import send_mail
from django.conf import settings

def send_custom_email(subject, message, recipient_list, from_email=None, fail_silently=False):
    """
    Send an email using Django's send_mail function.

    :param subject: Subject of the email
    :param message: Body of the email
    :param recipient_list: List of recipient email addresses
    :param from_email: The sender's email address (optional)
    :param fail_silently: Boolean to specify whether to fail silently or raise an exception (optional)
    """
    if from_email is None:
        from_email = settings.EMAIL_HOST_USER

    send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        fail_silently=fail_silently,
    )
