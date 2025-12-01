from django.urls import path
from . import views

urlpatterns = [
    path('', views.PetListView, name='pets'),
    path('add',views.create_my_pets_object, name='newpet'),
    path('profile/<int:id>',views.pet_profile, name='petprofile'),
    path('delete/<int:pk>/<int:id>',views.Delete_Pets_Object, name='deletepet'),
]