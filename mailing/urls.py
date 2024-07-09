from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MailingMessageListView, MailingMessageCreateView, MailingMessageDetailView, \
    MailingMessageUpdateView, MailingMessageDeleteView, MailingSettingsCreateView, MailingSettingsUpdateView, \
    MailingSettingsListView, MailingSettingsDetailView, MailingSettingsDeleteView

app_name = MailingConfig.name

urlpatterns = [
    path('', MailingMessageListView.as_view(), name='list'),
    path('create/', MailingMessageCreateView.as_view(), name='create'),
    path('<int:pk>/', MailingMessageDetailView.as_view(), name='view'),
    path('<int:pk>/update/', MailingMessageUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', MailingMessageDeleteView.as_view(), name='delete'),
    path('settings/', MailingSettingsListView.as_view(), name='settings_list'),
    path('settings/create/', MailingSettingsCreateView.as_view(), name='settings_create'),
    path('settings/<int:pk>/', MailingSettingsDetailView.as_view(), name='settings_view'),
    path('settings/<int:pk>/update/', MailingSettingsUpdateView.as_view(), name='settings_edit'),
    path('settings/<int:pk>/delete/', MailingSettingsDeleteView.as_view(), name='settings_delete'),
]