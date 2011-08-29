#-*- coding: utf-8 -*-
from django import forms
from subscription.models import Subscription
from django.utils.translation import ugettext_lazy as _
from subscription import validators
from django.core.validators import EMPTY_VALUES

class PhoneWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        widgets = (
            forms.TextInput(attrs=attrs),
            forms.TextInput(attrs=attrs))
        super(PhoneWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return value.split('-')
        return [None, None]

class PhoneField(forms.MultiValueField):
    widget = PhoneWidget

    def __init__(self, *args, **kwargs):
        fields = (
            forms.IntegerField(),
            forms.IntegerField())
        super(PhoneField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            if data_list[0] in EMPTY_VALUES:
                raise forms.ValidationError(u'DDD inválido.')
            if data_list[1] in EMPTY_VALUES:
                raise forms.ValidationError(u'Número inválido.')
            return '%s-%s' % tuple(data_list)
        return None


#6 - ModelForm completo
class SubscriptionForm(forms.ModelForm):
    phone = PhoneField(required=False)

    class Meta:
        model = Subscription
        exclude = ('created_at', 'paid')

    def clean(self):
        super(SubscriptionForm, self).clean()

        if not self.cleaned_data.get('email') and \
           not self.cleaned_data.get('phone'):
            raise forms.ValidationError(
                _(u'Você precisa informar seu e-mail ou seu telefone.'))
        return self.cleaned_data
