from django.urls import path
from . import views

urlpatterns = [
    path('logs/<int:id>', views.PetLogListView, name='logs'),
    path('edit/<int:pk>/<int:id>', views.edit_PetLogEntry, name='editpetlog'),
    path('new/<int:id>',views.create_logEntry_object, name='newpetlog'),
    path('delete/<int:pk>/<int:id>', views.Delete_LogEntry_Object, name='deletepetlog'),
]