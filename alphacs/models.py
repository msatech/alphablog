from django.db import models

# Create your models here.
class Contact(models.Model):
    subject = models.TextField()
    name = models.TextField()
    email = models.CharField(max_length=100)
    phone = models.TextField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email