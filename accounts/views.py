from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.models import User
from django.views import generic
from django.shortcuts import get_object_or_404


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class ProfileDetailView(generic.DetailView):
    model = User
    template_name = 'accounts/profile.html'
    context_object_name = 'user'

    def get_object(self):
        return get_object_or_404(User, pk=self.kwargs['id'])
        
    '''
    def get_context_data(self, **kwargs):
        return super(ProfileDetailView, self).get_context_data(**kwargs)
    '''