from django.urls import path
from . import views


urlpatterns = [
    path('vendor/<int:pk>/', views.VendorView.as_view()),
    path('vendor/create/', views.VendorCreateView.as_view()),
    path('vendor/', views.VendorListView.as_view()),
    path('vendor/specific/', views.VendorSpecificListView.as_view())
]
