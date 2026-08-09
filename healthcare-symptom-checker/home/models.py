from django.db import models

class SymptomSession(models.Model):
    patient_name = models.CharField(max_length=120)
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=20)
    symptoms = models.TextField()
    response = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient_name} - {self.created_at:%Y-%m-%d %H:%M}"
