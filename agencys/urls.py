from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='agency'),
    path('list/', views.agency_list, name='agency_list'),
    path('show/<int:id>/', views.agency_detail, name='agency_detail'),
    path('create/', views.create_agency, name='create_agency'),    
    path('edit/<int:id>/edit/', views.edit_agency, name='edit_agency'),
    path('delete/<int:id>/delete/', views.delete_agency, name='delete_agency'),
    path('addstaff/<int:id>/add_staff/', views.add_staff, name='add_staff'),
    
    
    # path('help/', views.agency_help, name='agency_help'),
    # path('contact/', views.agency_contact, name='agency_contact'),    
    # path('reports/', views.agency_reports, name='agency_reports'),
    # path('stats/', views.agency_stats, name='agency_stats'),
    
    # path('logs/<int:id>', views.PetLogListView, name='logs'),
    # path('logs/<int:id>', views.PetLogListView, name='logs'),
    # path('edit/<int:pk>/<int:id>', views.edit_PetLogEntry, name='editpetlog'),
    # path('new/<int:id>',views.create_logEntry_object, name='newpetlog'),
    # path('delete/<int:pk>/<int:id>', views.Delete_LogEntry_Object, name='deletepetlog'),
]