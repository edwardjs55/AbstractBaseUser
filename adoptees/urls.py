from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='adoption_home'),
    path('list/', views.adoption_list, name='adoption_list'),
    path('detail/<int:pk>/', views.detail_view, name='adoption_detail_view'),
    path('show/<int:id>/', views.adoption_detail, name='adoption_detail'),
    path('create/', views.create_adoption, name='adoption_create'),    
    path('edit/<int:id>/edit/', views.edit_adoption, name='adoption_update'),
    path('delete/<int:id>/delete/', views.delete_adoption, name='adoption_delete'),
    
]