from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailing.models import MailingMessage, MailingSettings, MailingStatus


class MailingMessageListView(ListView):
    model = MailingMessage


class MailingMessageDetailView(DetailView):
    model = MailingMessage


class MailingMessageCreateView(CreateView):
    model = MailingMessage
    fields = ('title', 'content')
    success_url = reverse_lazy('mailing:list')


class MailingMessageUpdateView(UpdateView):
    model = MailingMessage
    fields = ('title', 'content')
    success_url = reverse_lazy('mailing:list')


class MailingMessageDeleteView(DeleteView):
    model = MailingMessage
    success_url = reverse_lazy('mailing:list')


class MailingSettingsCreateView(CreateView):
    model = MailingSettings
    fields = ('sending', 'recipients', 'message', 'end_time')
    # form_class = MailingSettingsForm
    success_url = reverse_lazy('mailing:settings_list')


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
    fields = ('sending', 'recipients', 'message', 'end_time')
    # form_class = MailingSettingsForm
    success_url = reverse_lazy('mailing:settings_list')


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
class MailingSettingsListView(ListView):
    model = MailingSettings


class MailingSettingsDetailView(DetailView):
    model = MailingSettings


class MailingSettingsDeleteView(DeleteView):
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
