from django.db import models
from django.utils.text import slugify

class Reference(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=60, unique=True, blank=True)
    description = models.CharField(max_length=160, blank=True)

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Photo(models.Model):
    reference = models.ForeignKey(Reference, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='references/')
    alt_text = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.reference.name} - {self.id}'