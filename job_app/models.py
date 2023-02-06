from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

class job(models.Model):
    company = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250,null=False, unique_for_date='post_date', default="")
    post_date = models.DateField(auto_now=False, auto_now_add=True)
    closing_date = models.DateField()
    location = models.CharField(max_length=50)
    details = models.TextField()

    def __str__(self):
        return self.job_title+" - "+self.company
        
    def get_absolute_url(self):
        return reverse("job_detail", kwargs={"slug": self.slug})

    def save(self, *args,**kwargs):
        if not self.slug:
            self.slug  = slugify(self.job_title+" - "+self.company)
        return super().save(*args,**kwargs)
        

