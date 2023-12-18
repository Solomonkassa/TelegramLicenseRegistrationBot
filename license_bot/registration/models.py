from django.db import models

class UserProfile(models.Model):
    chat_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    license_key = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

