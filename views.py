from django.shortcuts import render
from .models import JobListing
# Create your views here.

def home(request):

    jobs_listings = JobListing.objects.all()

    return render(request, 'jobs_app/index.html', {'jobs_listings': jobs_listings})