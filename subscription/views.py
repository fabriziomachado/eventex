from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from subscription.forms import SubscriptionForm
from subscription.models import Subscription
from subscription.utils import send_subscription_email

def new(request):
    form = SubscriptionForm(initial={
        'name': 'Entre o seu nome',
        'cpf': 'Digite o seu CPF sem pontos',
        'email': 'Informe o seu email',
        'phone': '21-96186180',
    })
    context = RequestContext(request, {'form': form})
    return render_to_response('subscription/new.html', context)

def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        context = RequestContext(request, {'form': form})
        return render_to_response('subscription/new.html', context)

    subscription = form.save()
    
    send_subscription_email(subscription)
    return HttpResponseRedirect(reverse('subscription:success', args=[ subscription.pk ]))

def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def success(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    context = RequestContext(request, {'subscription': subscription})
    return render_to_response('subscription/success.html', context)
