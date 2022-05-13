from django.forms import ModelForm
from hotel.models import FoodDetail,Food
from django import forms



class Foodform(ModelForm):
    class Meta:
        model = Food
        fields = "__all__"

class Fooddetailform(ModelForm):
    class Meta:
        model = FoodDetail
        fields = "__all__"