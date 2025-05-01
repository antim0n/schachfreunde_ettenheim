from django.db import models

class Artikel(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    image_description = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date']