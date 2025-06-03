from django.db import models
from django.contrib.auth.models import User

class Epaper(models.Model):
    title = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to='epapers/')  # Upload path
    description = models.TextField(blank=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} - {self.date}"
