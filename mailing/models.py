from django.db import models

from recipient.models import Recipient

NULLABLE = {'null': True, 'blank': True}

MAILING_FREQUENCY = [('once', 'одинократно'), ('daily', 'раз в день'), ('weekly', 'раз в неделю'),
                     ('monthly', 'раз в месяц'), ]
MAILING_STATUS = [("Create", 'Создана'), ("Started", 'Отправлена'), ("Completed", 'Завершена'), ]
LOGS_STATUS_CHOICES = [('success', 'успешно'), ('fail', 'неуспешно'), ]


class MailingMessage(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовок',
        help_text='Введите заголовок сообщения'
    )
    content = models.TextField(
        verbose_name='Содержание',
        help_text='Введите текст сообщения'
    )

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.title


class MailingSettings(models.Model):
    start_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Начало рассылки'
    )
    end_time = models.DateTimeField(
        verbose_name='Конец рассылки',
        **NULLABLE
    )
    sending = models.CharField(
        max_length=100,
        choices=MAILING_FREQUENCY,
        verbose_name='Частота рассылки'
    )
    message = models.ForeignKey(
        MailingMessage,
        on_delete=models.CASCADE,
        verbose_name='Сообщение'
    )
    setting_status = models.CharField(
        max_length=50,
        choices=MAILING_STATUS,
        verbose_name='Статус рассылки',
        default='Create'
    )
    recipients = models.ManyToManyField(
        Recipient,
        verbose_name='Получатели'
    )

    class Meta:
        verbose_name = 'Настройка рассылки'
        verbose_name_plural = 'Настройки рассылок'

    def __str__(self):
        return f'{self.message} отправляется {self.sending} с {self.start_time}'


class MailingStatus(models.Model):
    last_sending_try = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время последней попытки')
    status = models.CharField(verbose_name='Статус попытки', choices=LOGS_STATUS_CHOICES)
    server_response = models.TextField(verbose_name='Ответ почтового сервера')
    mailing_list = models.ForeignKey(MailingSettings, on_delete=models.CASCADE, verbose_name='Рассылка')
    client = models.ForeignKey(Recipient, on_delete=models.CASCADE, verbose_name='Клиент рассылки', **NULLABLE)

    class Meta:
        verbose_name = 'Статус отправки'
        verbose_name_plural = 'Статусы отправки'

    def __str__(self):
        return f'{self.status} отправлялось {self.last_sending_try}, ответ сервера: {self.server_response}'
