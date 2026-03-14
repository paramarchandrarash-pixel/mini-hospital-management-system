from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    ROLE_CHOICES = (
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"


class Slot(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_slots')
    date = models.DateField()
    time = models.TimeField()
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.doctor.username} - {self.date} {self.time}"


class Booking(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_bookings')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_bookings')
    slot = models.OneToOneField(Slot, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.username} booked {self.doctor.username} - {self.slot.date} {self.slot.time}"