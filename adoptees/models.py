from django.db import models
from agencys.models import Agency
class Adoptee(models.Model):
    
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, related_name='adoptions',verbose_name='Agency')
    agency_pet_name = models.CharField(max_length=30,verbose_name='Agency Pet Name')
    adopted_pet_name = models.CharField(max_length=30, blank=True, null=True, default='Unknown',verbose_name='Adopted Name')
    pet_type = models.CharField(max_length=30, blank=True, null=True, default='Unknown',verbose_name='Pet Type')
    pet_gender = models.CharField(max_length=30, blank=True, null=True, default='Unknown',verbose_name='Pet Gender')
    pet_date_of_birth = models.DateField(blank=True, null=True,verbose_name='Date of Birth')    
    pet_place_of_birth = models.CharField(max_length=30, blank=True, null=True, default='Unknown',verbose_name='Birth Location')
    pet_photo = models.ImageField(blank=True,upload_to='adoptions/', default='adoptions/default.jpg',verbose_name='Pet Photo Image Links')
    # pet_photo = models.TextField(blank=True, null=True, default='None',verbose_name='Pet Photo Links')
    
    pet_surrender_date = models.DateField(blank=True, null=True,verbose_name='Date of Surrender')
    pet_surrenders_name = models.CharField(max_length=30, blank=True, null=True, default='Unknown',verbose_name='Pet From')
    pet_source = models.CharField(max_length=30, blank=True, null=True, default='Unknown',verbose_name='Pet Source Info')
    
    pet_description = models.TextField(blank=True, null=True, default='None',verbose_name='Pet Description')
    pet_color = models.CharField(max_length=30, blank=True, null=True, default='Unknown',verbose_name='Pet Color')
    pet_size = models.CharField(max_length=30, blank=True, null=True, default='Unknown',verbose_name='Pet Size')
    pet_weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,verbose_name='Pet Weight')
    pet_markings = models.TextField(blank=True, null=True, default='None',verbose_name='Pet Markings')
    pet_temperament = models.TextField(blank=True, null=True, default='None',verbose_name='Pet Temperament')
    pet_behavior_issues = models.TextField(blank=True, null=True, default='None',verbose_name='Behavior Issues')
    
    health_issues = models.TextField(blank=True, null=True, default='None',verbose_name='Health Issues')
    special_needs = models.TextField(blank=True, null=True, default='None',verbose_name='Special Needs')
    notes = models.TextField(blank=True, null=True, default='None',verbose_name='Additional Notes')

    # vaccinations/Shots and Spay/Neuter / ?? vaccinations administered_by ?? // Vouchers for free spay/neuter
    pet_microchip_id = models.CharField(max_length=80, blank=True, null=True, default='Unknown',verbose_name='Microchip ID')
    pet_vaccinations = models.TextField(blank=True, null=True, default='None',verbose_name='Vaccinations List')
    pet_vaccinations_date = models.DateField(blank=True, null=True,verbose_name='Vaccinations Date')
    pet_spayed_neutered = models.BooleanField(default=False,verbose_name='Spayed/Neutered Status')
    pet_spay_neuter_date = models.DateField(blank=True, null=True,verbose_name='Spay/Neuter Date')
    pet_spay_neuter_clinic = models.CharField(max_length=100, blank=True, null=True, default='Unknown',verbose_name='Spay/Neuter Clinic')
    
    vet_name = models.CharField(max_length=30,blank=True, null=True,verbose_name='Veterinarian Name')
    vet_contact_info = models.CharField(max_length=100, blank=True, null=True, default='Unknown',verbose_name='Veterinarian Contact Info')
    vet_med_notes = models.TextField(blank=True, null=True, default='None',verbose_name='Veterinarian Medical Notes')
    vet_medical_treatments = models.TextField(blank=True, null=True, default='None',verbose_name='Medical Treatments')
    vet_bill_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,verbose_name='Veterinarian Bill Amount')
    vet_visit_date = models.DateField(blank=True, null=True,verbose_name='Veterinarian Visit Date')
    
    last_vet_visit = models.DateField(blank=True, null=True,verbose_name='Last Veterinarian Visit Date')
    next_vet_visit = models.DateField(blank=True, null=True,verbose_name='Next Veterinarian Visit Date')
    
    pet_adopted = models.BooleanField(default=False,verbose_name='Adoption Status')
    pet_adoption_status = models.CharField(max_length=100, blank=True, null=True, default='Unknown',verbose_name='Post-Adoption Status')
    pet_adopted_date = models.DateField(blank=True, null=True,verbose_name='Date of Adoption')
    
    pet_adoptor_first_name = models.CharField(max_length=30, blank=True, null=True, default='Unknown',verbose_name='Pet Adoptor Name')
    pet_adoptor_last_name = models.CharField(max_length=30, blank=True, null=True, default='Unknown',verbose_name='Pet Adoptor Last Name')
    pet_adoptor_age = models.IntegerField(blank=True, null=True,verbose_name='Adoptor Age')
    pet_adoptor_contact = models.CharField(max_length=100, blank=True, null=True, default='Unknown',verbose_name='Pet Adoptor Contact Info')
    pet_adoptor_address = models.CharField(max_length=200, blank=True, null=True, default='Unknown',verbose_name='Pet Adoptor Address')
    pet_adoptor_email = models.CharField(max_length=100, blank=True, null=True, default='Unknown',verbose_name='Pet Adoptor Email')
    pet_adoptor_notes = models.TextField(blank=True, null=True, default='None',verbose_name='Adoptor Additional Notes')
    
    pet_adoption_location = models.CharField(max_length=100, blank=True, null=True, default='Unknown',verbose_name='Adoption Location')
    pet_adoption_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,verbose_name='Adoption Fee')
    pet_adoption_method = models.CharField(max_length=100, blank=True, null=True, default='Unknown',verbose_name='Adoption Method')
    pet_adoption_followup = models.TextField(blank=True, null=True, default='None',verbose_name='Follow-up Notes')
    
    pet_adoption_feedback = models.TextField(blank=True, null=True, default='None',verbose_name='Adoption Feedback')
    pet_adoption_photos = models.TextField(blank=True, null=True, default='None',verbose_name='Adoption Photos Links')
    pet_adoption_documents = models.TextField(blank=True, null=True, default='None',verbose_name='Adoption Documents Links')
    pet_adoption_agreement = models.TextField(blank=True, null=True, default='None',verbose_name='Adoption Agreement Details')
    pet_adoption_returned = models.BooleanField(default=False,verbose_name='Returned After Adoption')
    pet_adoption_return_date = models.DateField(blank=True, null=True,verbose_name='Return Date After Adoption')
    pet_adoption_return_reason = models.TextField(blank=True, null=True, default='None',verbose_name='Reason for Return After Adoption')
    pet_adoption_final_status = models.CharField(max_length=100, blank=True, null=True, default='Unknown',verbose_name='Final Status After Adoption Process')
    pet_adoption_notes = models.TextField(blank=True, null=True, default='None',verbose_name='Final Adoption Notes')
    
    record_created_at = models.DateTimeField(auto_now_add=True,verbose_name='Record Created At')
    record_updated_at = models.DateTimeField(auto_now=True,verbose_name='Record Updated At')
    record_active = models.BooleanField(default=True,verbose_name='Is Record Active')    
    
    pet_deceased = models.BooleanField(default=False,verbose_name='Is Pet Deceased')
    pet_deceased_date = models.DateField(blank=True, null=True,verbose_name='Pet Deceased Date')
    
    
    def __str__(self):
        return f"{self.agency_pet_name} // {self.adopted_pet_name}"
    
    
    