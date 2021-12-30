from django.db import models

# Create your models here.
class Quote(models.Model):

    content = models.TextField()
    source = models.CharField(max_length=256)
    date_added = models.DateTimeField(auto_now_add=True)
    pending = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)