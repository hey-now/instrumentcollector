from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('instruments/', views.instruments_index, name='index'),
    path('instruments/<int:instrument_id>', views.instruments_detail, name='detail'),
    path('instruments/create/', views.InstrumentCreate.as_view(), name='instruments_create'),
]