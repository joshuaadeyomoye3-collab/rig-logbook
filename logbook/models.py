from django.db import models

class ShiftLog(models.Model):
    SHIFT_CHOICES = [
        ('day', 'Day'),
        ('night', 'Night'),
    ]

    engineer_name = models.CharField(max_length=100)
    shift_date = models.DateField()
    shift_type = models.CharField(max_length=10, choices=SHIFT_CHOICES)
    equipment_status = models.TextField(blank=True)
    incidents = models.TextField(blank=True)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-shift_date']

    def __str__(self):
        return f"{self.engineer_name} — {self.shift_date} ({self.shift_type} shift)"