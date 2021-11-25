from django.urls import path
from . import views

app_name = 'motorpool'

urlpatterns = [
    path('brand-list/', views.brand_list),
    path('brand-detail/<int:pk>/', views.brand_detail, name='brand_detail')
]
