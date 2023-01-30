from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Food(models.Model):
    FLAVOR_CHOICES = [
        ('Life_changing', 'Life-changing'),
        ('Burstin', 'Bursting'),
        ('Hmmm', 'Hmmmm'),
        ('Need_salt', 'Needs salt'),
        ('Air', 'Air has more flavor')
    ]
    name = models.CharField(max_length=64)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    flavor = models.CharField(max_length=15, choices=FLAVOR_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.name
