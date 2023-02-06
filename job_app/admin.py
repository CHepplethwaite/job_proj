from django.contrib import admin
from .models import job

class jobAdmin(admin.ModelAdmin):
    list_display=('job_title',"post_date")
    prepopulated_fields={"slug":("job_title",)}

admin.site.register(job,jobAdmin)
