# Generated by Django 5.0.6 on 2024-06-16 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipient', '0002_remove_recipient_description_remove_recipient_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipient',
            name='comment',
            field=models.TextField(blank=True, help_text='Напишите комментарий', null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='recipient',
            name='full_name',
            field=models.CharField(default='', help_text='Введите имя', max_length=100, verbose_name='Имя'),
        ),
    ]
