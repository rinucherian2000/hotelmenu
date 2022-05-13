from django.shortcuts import render
from hotel.models import Food,FoodDetail
from django.views.generic import View, ListView, UpdateView, DeleteView, CreateView, DetailView
from django.urls import reverse_lazy
from hotel.form import Foodform,Fooddetailform

# Create your views here.
class FoodNameView(CreateView):
    model =Food
    form_class = Foodform
    template_name = "food_add.html"
    success_url = reverse_lazy('additem')

class FoodItemView(CreateView):
    model = FoodDetail
    form_class = Fooddetailform
    template_name = 'food_item.html'
    success_url = reverse_lazy('list')

class FoodList(ListView):
    model = FoodDetail
    context_object_name = "item"
    template_name = "avail_foods.html"

class Foodchange(UpdateView):
    model = FoodDetail
    form_class = Fooddetailform
    template_name = "foodedit.html"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('list')

class Fooddelete(DeleteView):
    model = FoodDetail
    template_name = 'fooddelete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("list")



