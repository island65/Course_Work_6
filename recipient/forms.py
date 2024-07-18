from django import forms


from common.views import StyleFormMixin
from recipient.models import Recipient


class RecipientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Recipient
        fields = ("full_name", "email", "comment")
