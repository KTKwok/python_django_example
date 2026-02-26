from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import TourCategory
from public_app.decorators import AllowedUserMixin

class TourCategoryListView(ListView):
    model = TourCategory
    context_object_name = "tour_categories"
    template_name = "tour_app/category/list.html"

class TourCategoryDetailView(DetailView):
    model = TourCategory
    context_object_name = "tour_category"
    template_name = "tour_app/category/detail.html"

class TourCategoryCreateView(LoginRequiredMixin, AllowedUserMixin, CreateView):
    allowed_roles = ['M', 'O']
    model = TourCategory
    fields = "__all__"
    template_name = "tour_app/category/form.html"
    success_url = reverse_lazy("tour_app:tour_categories")

class TourCategoryUpdateView(LoginRequiredMixin, AllowedUserMixin, UpdateView):
    allowed_roles = ['M', 'O']
    model = TourCategory
    fields = "__all__"
    template_name = "tour_app/category/form.html"
    success_url = reverse_lazy("tour_app:tour_categories")

class TourCategoryDeleteView(LoginRequiredMixin, AllowedUserMixin, DeleteView):
    allowed_roles = ['M']
    model = TourCategory
    template_name = "tour_app/category/delete.html"
    success_url = reverse_lazy("tour_app:tour_categories")