from django.db import models

class UserDetails(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    description = models.TextField(blank=True, null=True)  # Optional field

    def __str__(self):
        return self.full_name
