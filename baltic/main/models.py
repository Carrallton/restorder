from django.db import models

class Worker(models.Model):
    first_name = models.CharField("First name", max_length=255)
    last_name = models.CharField("Last name", max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    description = models.CharField(blank=True, null=True, max_length=255)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name
