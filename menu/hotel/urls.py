from django.urls import path
from hotel import views


urlpatterns = [
    path("add",views.FoodNameView.as_view(),name="add"),
    path("add/item",views.FoodItemView.as_view(),name="additem"),
    path("list",views.FoodList.as_view(),name="list"),
    path('edit/<int:id>',views.Foodchange.as_view(),name="change"),
    path("delete/<int:id>", views.Fooddelete.as_view(), name="delete"),


]