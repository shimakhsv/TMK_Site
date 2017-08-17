from django.db import models

class Contact(models.Model):
    email=models.EmailField()
    message=models.TextField()

    def __unicode__(self):
        return self.email
