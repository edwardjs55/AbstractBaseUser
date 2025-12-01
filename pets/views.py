from itertools import count
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from .forms import MyPetsForm
from .models import MyPets
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

def home(request):
    # template = loader.get_template('pets/pets_home.html')
    # return HttpResponse(template.render())
    content = [[pets.name,pets.animal_type,pets.description] for pets in MyPets]
    return render(request,'pets/pets_home.html',content)

def PetListView(request):
    model = MyPets
    template_name = 'pets/pets_home.html'
    context_object_name = 'pet_list'
    id = request.user.id
    # queryset = MyPets.objects.all()
    queryset = MyPets.objects.filter(user_id=id)
    if queryset.count() == 0:
        #queryset = [] #MyPets.objects.none()
        return render(request, template_name)
    queryset = list(queryset.values())
    #queryset = list((MyPets.objects.filter(user_id=id)).values())
    #print("id=",id, '    queryset=',queryset[0])
    return render(request, template_name, {context_object_name: queryset})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pets_list'] = MyPets.objects.all()
        return context 
    

def create_my_pets_object(request):
        if request.method == 'POST':
            form = MyPetsForm(request.POST)
            if form.is_valid():
                # form.save() # This creates and saves a new MyObject instance
                obj = form.save(commit=False)
                obj.user = request.user
                obj.save()                
                return redirect('pets') # Redirect to a success page
        else:
            form = MyPetsForm()
        return render(request, 'pets/add_new_pet.html', {'form': form})
    
 # obsolete ??   
def logs(request):
    template = loader.get_template('pets/logs.html')
    return render(request, 'pets/logs.html')

def Delete_Pets_Object(request,pk,id):
    obj = get_object_or_404(MyPets, pk=pk) # Retrieve the object to delete
    if request.method == 'POST':
        print("Deleted Pet with name = ",obj.name,' id ',obj.id)
        obj.delete() # Delete the object
        return redirect('pets') # Redirect to a success page
    return render(request, 'pets/delete_pet.html', {'object': obj})

@login_required
def pet_profile(request,id):
    # pet = MyPets.objects.filter(id=id)
    
    obj = get_object_or_404(MyPets, id=id) # Retrieve the object to edit
    print(obj.name)
    if request.method == 'POST':
        form = MyPetsForm(request.POST, instance=obj) # Bind submitted data to the form, with the existing object as instance
        if form.is_valid():
            form.save() # Save changes to the existing object
            return redirect('pets') # Redirect to a success page or object detail
    else:
        form = MyPetsForm(instance=obj) # Initialize form with existing object data for display
    
    return render(request, 'pets/pet_profile.html', {'form': form})