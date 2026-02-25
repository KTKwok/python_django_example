from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Destination
from public_app.decorators import AllowedUserMixin

class DestinationListView(ListView):
    model = Destination
    context_object_name = "destinations"
    template_name = "tour_app/destination/list.html"
    #queryset = Destination.objects.filter(is_featured=True)

class DestinationDetailView(DetailView):
    model = Destination
    context_object_name = "destination"
    template_name = "tour_app/destination/detail.html"

class DestinationCreateView(LoginRequiredMixin, AllowedUserMixin, CreateView):
    allowed_roles = ['M', 'O']
    model = Destination
    fields = "__all__"
    template_name = "tour_app/destination/form.html"
    success_url = reverse_lazy("tour_app:destinations")

class DestinationUpdateView(LoginRequiredMixin, AllowedUserMixin, UpdateView):
    allowed_roles = ['M', 'O']
    model = Destination
    fields = "__all__"
    template_name = "tour_app/destination/form.html"
    success_url = reverse_lazy("tour_app:destinations")

class DestinationDeleteView(LoginRequiredMixin, AllowedUserMixin, DeleteView):
    allowed_roles = ['M', 'O']
    model = Destination
    template_name = "tour_app/destination/delete.html"
    success_url = reverse_lazy("tour_app:destinations")