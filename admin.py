from django.contrib import admin
from.models import (
    JobListing,
)


class JobListingAdmin(admin.ModelAdmin):
    List_display = ('title', 'description')


admin.site.register(JobListing, JobListingAdmin)
