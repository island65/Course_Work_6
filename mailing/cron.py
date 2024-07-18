import smtplib
from django.core.mail import send_mail
from datetime import datetime, timedelta
import pytz
from config import settings
from mailing.models import MailingSettings, MailingStatus, LOGS_STATUS_CHOICES


def send_mailing():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)

    mailings = MailingSettings.objects.filter(start_time__lte=current_datetime).filter(setting_status__in=['Create'])
    for mailing in mailings:
        title = mailing.message.title
        content = mailing.message.content
        mailing.setting_status = 'Started'
        mailing.save()
        try:
            server_response = send_mail(
                subject=title,
                message=content,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[client.email for client in mailing.recipients.all()],
                fail_silently=False)
            if server_response == 1:
                server_response = 'Письмо успешно отправлено'
                MailingStatus.objects.create(status=LOGS_STATUS_CHOICES[0][1], server_response=server_response,
                                             mailing_list=mailing)
            mailing.setting_status = 'Create'

            if mailing.sending == 'once' and server_response == 1:
                mailing.start_time = current_datetime
                mailing.setting_status = 'Create'

            elif mailing.sending == 'daily' and server_response == 1:
                current_datetime = MailingSettings.objects.get(sending='daily')
                mailing.start_time = current_datetime.start_time + timedelta(days=1)
                mailing.setting_status = 'Create'

            elif mailing.sending == 'weekly' and server_response == 1:
                current_datetime = MailingSettings.objects.get(sending='weekly')
                mailing.start_time = current_datetime.start_time + timedelta(days=7)
                mailing.setting_status = 'Create'

            elif mailing.sending == 'monthly' and server_response == 1:
                current_datetime = MailingSettings.objects.get(sending='monthly')
                mailing.start_time = current_datetime.start_time + timedelta(days=30)
                mailing.setting_status = 'Create'

            mailing.save()

        except smtplib.SMTPException as error:
            MailingStatus.objects.create(status=LOGS_STATUS_CHOICES[1][1], server_response=error, mailing_list=mailing)
            mailing.setting_status = 'Create'
