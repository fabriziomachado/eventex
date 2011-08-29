#-*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
#from subscription import validators

class Subscription(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(_('pago'))
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        ordering = ["created_at"]
        verbose_name = u"Inscrição"
        verbose_name_plural = u"Inscrições" 
