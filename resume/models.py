from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    proj_image = CloudinaryField('image')
    repo_link = models.URLField()
    proj_link = models.URLField()
    

    class Meta:
        verbose_name = ("project")
        verbose_name_plural = ("project")

    def __str__(self):
        return self.title

    