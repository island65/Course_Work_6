from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Recipient(models.Model):
    email = models.EmailField(
        verbose_name='Почта',
        unique=True,
        help_text='Введите почту'
    )
    full_name = models.CharField(
        max_length=100,
        verbose_name='Имя',
        default='',
        help_text='Введите имя'
    )
    comment = models.TextField(
        verbose_name='Комментарий',
        **NULLABLE,
        help_text='Напишите комментарий'
    )

    class Meta:
        verbose_name = 'Получатель'
        verbose_name_plural = 'Получатели'

    def __str__(self):
        return f'{self.full_name} ({self.email})'
