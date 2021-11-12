from django.urls import path
from . import views

urlpatterns = [
    path('brand-list/', views.brand_list),
]
