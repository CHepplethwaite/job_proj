from django.db import models

class job(models.Model):
    company = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    closing_date = models.DateField()
    location = models.CharField(max_length=50)
    details = models.TextField()