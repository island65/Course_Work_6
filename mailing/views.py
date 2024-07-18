from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from mailing.forms import MailingSettingsForm, MailingMessageForm, MailingModeratorForm
from mailing.models import MailingMessage, MailingSettings, MailingStatus
from mailing.servives import get_blog_from_cache
from recipient.models import Recipient


class MailingMessageTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'mailing/home.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['blogs'] = get_blog_from_cache()
        mailing_settings = MailingSettings.objects.all()
        context_data['mailing_settings'] = len(mailing_settings)
        active_mailing = MailingSettings.objects.filter(setting_status='Started')
        context_data['active_mailing'] = len(active_mailing)
        recipients = Recipient.objects.all()
        context_data['recipient'] = len(recipients)
        return context_data


class MailingMessageListView(LoginRequiredMixin, ListView):
    model = MailingMessage


class MailingMessageDetailView(LoginRequiredMixin, DetailView):
    model = MailingMessage


class MailingMessageCreateView(LoginRequiredMixin, CreateView):
    model = MailingMessage
    form_class = MailingMessageForm
    success_url = reverse_lazy('mailing:list')

    def form_valid(self, form):
        message = form.save()
        message.owner = self.request.user
        message.save()
        return super().form_valid(form)


class MailingMessageUpdateView(LoginRequiredMixin, UpdateView):
    model = MailingMessage
    form_class = MailingMessageForm
    success_url = reverse_lazy('mailing:list')


class MailingMessageDeleteView(LoginRequiredMixin, DeleteView):
    model = MailingMessage
    success_url = reverse_lazy('mailing:list')


class MailingSettingsCreateView(LoginRequiredMixin, CreateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('mailing:settings_list')

    def form_valid(self, form):
        setting = form.save()
        setting.owner = self.request.user
        setting.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


#
#     def form_valid(self, form):
#         """Сохранение создателя сообщения"""
#         mailing_settings = form.save()
#         user = self.request.user
#         mailing_settings.creator = user
#         mailing_settings.save()
#         return super().form_valid(form)
#
#
class MailingSettingsUpdateView(LoginRequiredMixin, UpdateView):
    model = MailingSettings
    form_class = MailingSettingsForm

    def get_success_url(self):
        mailing = self.get_object()
        return reverse('mailing:settings_view', args=[mailing.pk])

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner or user.is_superuser:
            return MailingSettingsForm
        if user.has_perm('mailing.change_mailingsettings_setting_status'):
            return MailingModeratorForm
        return PermissionDenied


#
#     def get_form_class(self):
#         """Переопределяем форму для модератора"""
#         user = self.request.user
#         if user == self.object.creator:
#             return MailingSettingsForm
#         if user.has_perm('mailing.can_change_settings_status'):
#             return MailingSettingsModeratorForm
#         raise PermissionDenied
#
#
class MailingSettingsListView(LoginRequiredMixin, ListView):
    model = MailingSettings


class MailingSettingsDetailView(LoginRequiredMixin, DetailView):
    model = MailingSettings


class MailingSettingsDeleteView(LoginRequiredMixin, DeleteView):
    model = MailingSettings
    success_url = reverse_lazy('mailing:settings_list')


class MailingStatusListView(ListView):
    model = MailingStatus


class MailingStatusDeleteView(DeleteView):
    model = MailingStatus
    success_url = reverse_lazy('mailing:status_list')


class HomePageView(ListView):
    model = MailingSettings

#     def get_context_data(self, **kwargs):
#         """Получаем необходимые данные для домашней страницы"""
#         context = super().get_context_data(**kwargs)
#         queryset = self.get_queryset()
#         mailing_settings = queryset.filter()
#
#         mailing_settings_count = mailing_settings.count()
#         mailing_settings_active_count = mailing_settings.filter(settings_status='Started').count()
#         recipients_count = mailing_settings.values('recipients').distinct().count()
#
#         context['mailing_settings_count'] = mailing_settings_count
#         context['mailing_settings_active_count'] = mailing_settings_active_count
#         context['recipients_count'] = recipients_count
#         # context['blog_posts'] = get_three_random_blog(self.request)
#
#         return context
