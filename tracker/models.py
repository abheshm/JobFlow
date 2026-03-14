from django.db import models

# Create your models here.
class JobApplication(models.Model):

    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Interview', 'Interview'),
        ('Rejected', 'Rejected'),
        ('Offer', 'Offer'),

    ]

    company_name = models.CharField(max_length=100)
    job_role = models.CharField(max_length=100)
    application_date = models.DateField
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Applied')
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company_name} - {self.job_role}"