from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from recipient.models import Recipient


class RecipientListView(ListView):
    model = Recipient


class RecipientDetailView(DetailView):
    model = Recipient


class RecipientCreateView(CreateView):
    model = Recipient
    fields = ("email", "full_name", "comment")
    success_url = reverse_lazy('recipient:list')


class RecipientUpdateView(UpdateView):
    model = Recipient
    fields = ("email", "full_name", "comment")
    success_url = reverse_lazy('recipient:list')


class RecipientDeleteView(DeleteView):
    model = Recipient
    success_url = reverse_lazy('recipient:list')
