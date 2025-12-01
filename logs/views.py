from django.shortcuts import redirect, render, get_object_or_404
from .forms import MyPetsLogForm
from pets.models import MyPets
from .models import LogEntry

def home(request, id):
    name = MyPets.objects.get(id=id).name 
    pet = {'id': id, 'name':name}    
    return render(request, 'logs/home.html',{'pet':pet})

def edit_PetLogEntry(request,pk,id):
    name = MyPets.objects.get(id=id).name 
    pet = {'id': id, 'name':name}    
    obj = get_object_or_404(LogEntry, pk=pk) # Retrieve the object to edit

    if request.method == 'POST':
        form = MyPetsLogForm(request.POST, instance=obj) # Bind submitted data to the form, with the existing object as instance
        if form.is_valid():
            form.save() # Save changes to the existing object
            return redirect('logs',id=id) # Redirect to a success page or object detail
    else:
        form = MyPetsLogForm(instance=obj) # Initialize form with existing object data for display

    return render(request, 'logs/edit_PetLogEntry.html', {'form': form, 'object': obj, 'pet':pet})

    
def PetLogListView(request,id):
    name = MyPets.objects.get(id=id).name 
    pet = {'id': id, 'name':name} 
           
    model = LogEntry
    template_name = 'logs/home.html'
    context_object_name = 'pet_log_list'
    # queryset = MyPets.objects.all()
    queryset = model.objects.filter(pet=id)
    if queryset.count() == 0:
        #queryset = [] #MyPets.objects.none()
        return render(request, template_name,{'pet':pet})
    queryset = list(queryset.values())
    #queryset = list((MyPets.objects.filter(user_id=id)).values())
    #print("id=",id, '    queryset=',queryset[0])
    return render(request, template_name, {context_object_name: queryset, 'pet':pet})
    


def create_logEntry_object(request,id):
        name = MyPets.objects.get(id=id).name
        pet = {'id': id, 'name':name}
        if request.method == 'POST':
            form = MyPetsLogForm(request.POST)
            if form.is_valid():
                # form.save() # This creates and saves a new MyObject instance
                obj = form.save(commit=False)
                obj.pet = MyPets.objects.get(id=id) #request.user
                obj.save()                
                return redirect('logs',id=id) # Redirect to a success page
        else:
            form = MyPetsLogForm()
        return render(request, 'logs/add_new_log.html',{'form': form, 'pet':pet})
    

def Delete_LogEntry_Object(request,pk,id):
    obj = get_object_or_404(LogEntry, pk=pk) # Retrieve the object to delete
    if request.method == 'POST':
        obj.delete() # Delete the object
        return redirect('logs',id=id) # Redirect to a success page
    return render(request, 'logs/delete_logentry.html', {'object': obj})