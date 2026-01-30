from django.shortcuts import get_object_or_404, redirect, render
from .models import Adoptee
from .forms import Adoptee_Create_Form, Adoptee_Update_Form, Adoptee_Show_Form
from django.contrib.auth.decorators import login_required


def detail_view(request, pk):
    instance = Adoptee.objects.get(pk=pk)
    # Get all concrete fields for the model instance
    fields = instance._meta.concrete_fields
    field_data = []
    for field in fields:
        field_data.append({
            'verbose_name': field.verbose_name,
            'name': field.name,
            'value': getattr(instance, field.name) # Get the actual value
        })
    
    context = {
        'instance': instance,
        'field_data': field_data
    }
    return render(request, 'adoptees/detail_view.html', context)


def index(request):
    # content = [[Adoptee.agency_pet_name, Adoptee.adopted_pet_name,
    #             Adoptee.pet_adopted_date, Adoptee.pet_adoption_fee,
    #             Adoptee.pet_adoption_notes] for Adoptee in Adoptee.objects.all()]
    # print("Adoptee Index View Content:", content)
    content = Adoptee.objects.filter(agency_id=request.session['agency_id']).first()  # Fetch a single Adoptee instance for demonstration
    # print("Adoptee Index View Single Instance:", content)
    return render(request, 'adoptees/index.html', {'adoption': content})

def adoption_list(request):
    # print('session_agency_id=', request.session['agency_id'])
    content = Adoptee.objects.filter(agency_id=request.session['agency_id'])
    agency_name=content[0].agency
    return render(request, 'adoptees/list.html',{ 'adoptions': content, 'agency_name': agency_name })

def adoption_detail(request, id):
    obj = Adoptee.objects.get(pk=id)
    form = Adoptee_Show_Form(instance=obj)
    return render(request, 'adoptees/detail.html', { 'adoption': obj, 'form': form })

def create_adoption(request):
    if request.method == 'POST':
            form = Adoptee_Create_Form(request.POST)
            if form.is_valid():
                # form.save() # This creates and saves a new MyObject instance
                obj = form.save(commit=False)
                obj.agency_id = request.session['agency_id']  # Set the agency from session
                obj.user = request.user
                obj.save()                
                return redirect('adoption_detail_view', pk=obj.id) # Redirect to a success page
    else:
        form = Adoptee_Create_Form()
    return render(request, 'adoptees/create.html', {'adoption': form})

@login_required
def edit_adoption(request, id):
    obj = get_object_or_404(Adoptee, id=id) # Retrieve the object to edit
    #print(obj.name)
    if request.method == 'POST':
        form = Adoptee_Update_Form(request.POST,request.FILES, instance=obj) # Bind submitted data to the form, with the existing object as instance
        if form.is_valid():
            form.save() # Save changes to the existing object
            return redirect('adoption_detail_view', id) # Redirect to a success page or object detail
    else:
        form = Adoptee_Update_Form(instance=obj) # Initialize form with existing object data for display
    return render(request, 'adoptees/update.html', {'adoption': form, 'obj': obj})

def delete_adoption(request, id):
    adoption = Adoptee.objects.get(pk=id)
    if request.method == 'POST':
        adoption.delete()
        return redirect('adoption_list')  # Redirect to a success page after deletion
    return render(request, 'adoptees/delete.html', {'adoption': adoption})

