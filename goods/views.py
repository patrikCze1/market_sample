from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from .models import Offer, Comment


class IndexView(generic.ListView):
    model = Offer
    template_name = 'goods/index.html'
    context_object_name = 'offers'
    paginate_by = 20

    def get_queryset(self):
        query = self.request.GET.get('name')
        if not query:
            query = ''

        orderBy = self.request.GET.get('order')
        if not orderBy:
            orderBy = 'created_at'
        
        return Offer.objects.filter(name__contains=query).order_by(orderBy)


class DetailView(generic.DetailView):
    model = Offer
    template_name = 'goods/detail.html'
    context_object_name = 'offer'

    def get_queryset(self):
        return Offer.objects.filter()


#https://docs.djangoproject.com/en/2.2/topics/class-based-views/generic-editing/#models-and-request-user
@method_decorator(login_required, name='dispatch')
class OfferCreate(LoginRequiredMixin, CreateView):
    model = Offer
    template_name = 'goods/offer_form.html'
    fields = ['name', 'description', 'amount', 'price', 'currency']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('goods:detail', args = (self.object.id,)) # kwargs = {'pk': kwargs['idnumber']}


@method_decorator(login_required, name='dispatch')
class OfferUpdate(UpdateView):
    model = Offer
    template_name = 'goods/offer_update_form.html'
    fields = ['name', 'description', 'amount', 'price', 'currency']

    # passing id to BE
    def get_object(self, queryset=None):
        obj = Offer.objects.get(id=self.kwargs['id'])

        # check if user is owner
        if obj.user.id == self.request.user.id:
            return obj

        return HttpResponseNotFound('ahoj')

    # redirect
    def get_success_url(self):
        return reverse_lazy('goods:detail', args=(self.object.id,))

# todo overit id
@method_decorator(login_required, name='dispatch')
class OfferDelete(DeleteView):
    model = Offer
    success_url = reverse_lazy('goods:index')

    def get_object(self, queryset=None):
        obj = Offer.objects.get(id=self.kwargs['id'])
        return obj


@login_required
def sendComment(request, id):
    try:
        get_object_or_404(Offer, pk=id)
    except (KeyError, Offer.DoesNotExist):
        return render(request, 'goods/index.html', {
            'error_message': "Nastal problém.",
        })
    else:
        offer = Offer.objects.get(pk=id)
        Comment.objects.create(text=request.POST['text'], user=request.user, offer=offer)

        send_mail(
            offer.name + ' má nový komentář',
            'bbbbbbb.',
            'app@example.com',
            [offer.user.email,],
        )
        
        messages.add_message(request, messages.SUCCESS, 'Komentář přidán')
        return HttpResponseRedirect(reverse('goods:detail', args=(offer.id,)))


@login_required
def sendEmail(request, id):
    try:
        get_object_or_404(Offer, pk=id)
    except (KeyError, Offer.DoesNotExist):
        return render(request, 'goods/index.html', {
            'error_message': "Nastal problém, zkuste to znovu.",
        })
    else:
        offer = Offer.objects.get(pk=id)

        send_mail(
            offer.name + ' - nová zpráva',
            'Uživatel ' + str(request.user) + ' píše: \n' + str(request.POST['text']),
            request.user.email,
            [offer.user.email,],
        )
        
        messages.add_message(request, messages.SUCCESS, 'Zpráva odeslána')
        return HttpResponseRedirect(reverse('goods:detail', args=(offer.id,)))