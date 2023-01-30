# snippets/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from foods import views

urlpatterns = [
    path('foods/', views.FoodList.as_view(), name='food_list'),
    path('foods/<int:pk>/', views.FoodDetail.as_view(), name='food_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)