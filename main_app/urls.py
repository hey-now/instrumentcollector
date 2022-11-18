from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('instruments/', views.instruments_index, name='index'),
    path('instruments/guitars', views.instruments_guitars, name='guitars'),
    path('instruments/keyboards', views.instruments_keyboards, name='keyboards'),
    path('instruments/<int:instrument_id>', views.instruments_detail, name='detail'),
    path('instruments/create/', views.InstrumentCreate.as_view(), name='instruments_create'),
    path('instruments/<int:pk>/update/', views.InstrumentUpdate.as_view(), name='instruments_update'),
    path('instruments/<int:pk>/delete/', views.InstrumentDelete.as_view(), name='instruments_delete'),
    path('instruments/<int:instrument_id>/add_played/', views.add_played, name='add_played'),
    path('instruments/<int:instrument_id>/assoc_accessory/<int:accessory_id>/', views.assoc_accessory, name='assoc_accessory'),
    path('instruments/<int:instrument_id>/unassoc_accessory/<int:accessory_id>/', views.unassoc_accessory, name='unassoc_accessory'),
    path('accessories/', views.AccessoryList.as_view(), name='accessories_index'),
    path('accessories/<int:pk>/', views.AccessoryDetail.as_view(), name='accessories_detail'),
    path('accessories/create/', views.AccessoryCreate.as_view(), name='accessories_create'),
    path('accessories/<int:pk>/update/', views.AccessoryUpdate.as_view(), name='accessories_update'),
    path('accessories/<int:pk>/delete/', views.AccessoryDelete.as_view(), name='accessories_delete'),
]