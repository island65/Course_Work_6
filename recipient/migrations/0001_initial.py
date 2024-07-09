# Generated by Django 5.0.6 on 2024-05-10 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='Введите почту', max_length=254, unique=True, verbose_name='Почта')),
                ('name', models.CharField(help_text='Введите название категории', max_length=100, verbose_name='Имя')),
                ('description', models.TextField(blank=True, help_text='Введите описание категории', null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Получатель',
                'verbose_name_plural': 'Получатели',
            },
        ),
    ]
