from datetime import timedelta
from django.db import models

# Create your models here.

class Course(models.Model):
    courseName  = models.CharField(max_length=100, verbose_name='Course Name')
    courseImage = models.ImageField(upload_to='subjectimages', help_text='image size should be below 10mb', verbose_name='Course Image')
    coursePrice = models.PositiveIntegerField(help_text='Enter Price in dollars', verbose_name='Course Price')
    courseDuration = models.DurationField(default=timedelta(hours=6, minutes=20), verbose_name='Course Duration')

    def __str__(self):
        return self.courseName
