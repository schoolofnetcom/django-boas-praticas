from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from my_app.forms import AddressForm
from my_app.models.address import Address
from my_app.views import FormSubmittedInContextMixin


class AddressListView(LoginRequiredMixin, ListView):
    model = Address
    template_name = 'my_app/address/list.html'


class AddressDetailView(LoginRequiredMixin, DetailView):
    model = Address
    template_name = 'my_app/address/detail.html'


class AddressCreateView(LoginRequiredMixin, FormSubmittedInContextMixin, CreateView):
    model = Address
    # fields = ['address', 'address_complement', 'city', 'state', 'country']
    form_class = AddressForm
    template_name = 'my_app/address/create.html'
    success_url = reverse_lazy('my_app:address_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddressUpdateView(LoginRequiredMixin, FormSubmittedInContextMixin, UpdateView):
    model = Address
    # fields = ['address', 'address_complement', 'city', 'state', 'country']
    form_class = AddressForm
    template_name = 'my_app/address/update.html'
    success_url = reverse_lazy('my_app:address_list')


class AddressDeleteView(LoginRequiredMixin, DeleteView):
    model = Address
    template_name = 'my_app/address/destroy.html'
    success_url = reverse_lazy('my_app:address_list')