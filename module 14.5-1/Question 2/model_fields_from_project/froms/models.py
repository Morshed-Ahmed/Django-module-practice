from django.db import models

# Create your models here.
class JobsPost(models.Model):
    jobTitle = models.TextField(max_length=30)
    jobDescription = models.CharField(max_length=500)
    companyName = models.CharField(max_length=30)
    jobPosition = models.CharField(max_length=50)
    salary = models.CharField(max_length=10)
    postExpireDate = models.DateField()

    def __str__(self):
        return self.jobTitle
    

