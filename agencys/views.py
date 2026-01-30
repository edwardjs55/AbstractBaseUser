from django.utils import timezone
from django.shortcuts import redirect, render
from .forms import Agency_New_Form, Agency_Update_Form
from .models import Agency

# Create your views here.

def index(request):
    agency_id = request.session.get('agency_id', Agency.objects.filter(director=request.user).first().id)
    request.session['agency_id'] = agency_id  # Set the user's agencyprofile to the current agency
    #agency = Agency.objects.filter(director=request.user).first()    
    agency = Agency.objects.get(id=agency_id) #request.session['agency_id'])
    return render(request, 'agencys/index.html', {'agency': agency})

def agency_detail(request, id):
    agency = Agency.objects.get(id=id)
    request.session['agency_id'] = agency.id  # Set the user's agencyprofile to the current agency
    return render(request, 'agencys/agency_detail.html', {'agency': agency})

def agency_list(request):
    agencies = Agency.objects.filter(director=request.user)
    return render(request, 'agencys/agency_list.html', {'agencies': agencies})
      
def agency_admin_list(request):
    agencies = Agency.objects.all()
    return render(request, 'agencys/agency_list.html', {'agencies': agencies})      

def create_agency(request):
    if request.method == 'POST':
        form = Agency_New_Form(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.director = request.user
            obj.save()
            return redirect(obj.get_absolute_url())    
    else:
        form = Agency_New_Form()
    return render(request, 'agencys/create_agency.html', {'form': form})

def edit_agency(request, id):
    agency = Agency.objects.get(id=id)
    if request.method == 'POST':
        form = Agency_Update_Form(request.POST, instance=agency)
        if form.is_valid():
            agency = form.save(commit=False)
            agency.director = request.user
            agency.updated_at = timezone.now()
            agency.save()
            return redirect(agency.get_absolute_url())
    form = Agency_Update_Form(instance=agency)
    return render(request, 'agencys/edit_agency.html', {'agency': agency, 'form': form})

def delete_agency(request, id):
    agency = Agency.objects.get(id=id)
    if request.method == 'POST':
        agency.delete()
        return redirect('agency_list')
    return render(request, 'agencys/delete_agency.html', {'agency': agency})




def add_staff(request, id):
    agency = Agency.objects.get(id=id)
    if request.method == 'POST':
        staff_username = request.POST.get('staff_username')
        from django.contrib.auth import get_user_model
        User = get_user_model()
        try:
            staff_member = User.objects.get(username=staff_username)
            agency.staff.add(staff_member)
            agency.save()
            return redirect(agency.get_absolute_url())
        except User.DoesNotExist:
            error = "User does not exist"
            return render(request, 'agencys/add_staff.html', {'agency': agency, 'error': error})
    return render(request, 'agencys/add_staff.html', {'agency': agency})

def remove_staff(request, id, staff_id):    
    agency = Agency.objects.get(id=id)
    from django.contrib.auth import get_user_model
    User = get_user_model()
    try:
        staff_member = User.objects.get(id=staff_id)
        agency.staff.remove(staff_member)
        agency.save()
        return redirect(agency.get_absolute_url())
    except User.DoesNotExist:
        error = "User does not exist"
        return render(request, 'agencys/agency_detail.html', {'agency': agency, 'error': error})
    
def staff_list(request, id):
    agency = Agency.objects.get(id=id)
    staff_members = agency.staff.all()
    return render(request, 'agencys/staff_list.html', {'agency': agency, 'staff_members': staff_members})

def director_agencies(request):
    agencies = Agency.objects.filter(director=request.user)
    return render(request, 'agencys/director_agencies.html', {'agencies': agencies})

def staff_agencies(request):
    agencies = Agency.objects.filter(staff=request.user)
    return render(request, 'agencys/staff_agencies.html', {'agencies': agencies})

def agency_dashboard(request, id):
    agency = Agency.objects.get(id=id)
    return render(request, 'agencys/agency_dashboard.html', {'agency': agency}) 

def agency_reports(request, id):
    agency = Agency.objects.get(id=id)
    # Placeholder for report data
    reports = []
    return render(request, 'agencys/agency_reports.html', {'agency': agency, 'reports': reports})

def agency_settings(request, id):
    agency = Agency.objects.get(id=id)
    if request.method == 'POST':
        # Handle settings update
        pass
    return render(request, 'agencys/agency_settings.html', {'agency': agency})



""" Block Commented Out Functions- for future consideration
    - A/I generated suggestions saved for review

def agency_help(request):
    return render(request, 'agencys/agency_help.html')
def agency_contact(request):
    return render(request, 'agencys/agency_contact.html')
def agency_faq(request):
    return render(request, 'agencys/agency_faq.html')
def agency_terms(request):
    return render(request, 'agencys/agency_terms.html')
def agency_privacy(request):
    return render(request, 'agencys/agency_privacy.html')
def agency_about(request):
    return render(request, 'agencys/agency_about.html')
def agency_news(request):
    return render(request, 'agencys/agency_news.html')
def agency_events(request):
    return render(request, 'agencys/agency_events.html')
def agency_blog(request):
    return render(request, 'agencys/agency_blog.html')
def agency_careers(request):
    return render(request, 'agencys/agency_careers.html')
def agency_partners(request):
    return render(request, 'agencys/agency_partners.html')
def agency_testimonials(request):
    return render(request, 'agencys/agency_testimonials.html')
def agency_gallery(request):
    return render(request, 'agencys/agency_gallery.html')
def agency_resources(request):
    return render(request, 'agencys/agency_resources.html')
def agency_support(request):
    return render(request, 'agencys/agency_support.html')
def agency_feedback(request):
    return render(request, 'agencys/agency_feedback.html')
def agency_sitemap(request):
    return render(request, 'agencys/agency_sitemap.html')
def agency_press(request):
    return render(request, 'agencys/agency_press.html')
def agency_investors(request):
    return render(request, 'agencys/agency_investors.html')
def agency_social(request):
    return render(request, 'agencys/agency_social.html')
def agency_announcements(request):
    return render(request, 'agencys/agency_announcements.html')
def agency_policies(request):
    return render(request, 'agencys/agency_policies.html')
def agency_mission(request):
    return render(request, 'agencys/agency_mission.html')
def agency_values(request):
    return render(request, 'agencys/agency_values.html')
def agency_history(request):
    return render(request, 'agencys/agency_history.html')
def agency_team(request):
    return render(request, 'agencys/agency_team.html')
def agency_locations(request):
    return render(request, 'agencys/agency_locations.html')
def agency_services(request):
    return render(request, 'agencys/agency_services.html')
def agency_participate(request):
    return render(request, 'agencys/agency_participate.html')
def agency_donate(request):
    return render(request, 'agencys/agency_donate.html')
def agency_volunteer(request):
    return render(request, 'agencys/agency_volunteer.html')
def agency_events_calendar(request):
    return render(request, 'agencys/agency_events_calendar.html')
def agency_newsletter(request):
    return render(request, 'agencys/agency_newsletter.html')
def agency_media(request):
    return render(request, 'agencys/agency_media.html')
def agency_awards(request):
    return render(request, 'agencys/agency_awards.html')
def agency_initiatives(request):
    return render(request, 'agencys/agency_initiatives.html')
def agency_collaborations(request):
    return render(request, 'agencys/agency_collaborations.html')
def agency_future_plans(request):
    return render(request, 'agencys/agency_future_plans.html')
def agency_impact(request):
    return render(request, 'agencys/agency_impact.html')
def agency_stories(request):
    return render(request, 'agencys/agency_stories.html')
def agency_news_updates(request):
    return render(request, 'agencys/agency_news_updates.html')
def agency_contact_us(request):
    return render(request, 'agencys/agency_contact_us.html')
def agency_follow_us(request):
    return render(request, 'agencys/agency_follow_us.html')
def agency_subscribe(request):
    return render(request, 'agencys/agency_subscribe.html')
def agency_unsubscribe(request):
    return render(request, 'agencys/agency_unsubscribe.html')   
def agency_media_kit(request):
    return render(request, 'agencys/agency_media_kit.html')
  """   
    