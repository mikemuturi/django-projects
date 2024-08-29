from django.db import models
from datetime import timedelta
# from django.db.models import Count



class Subjects(models.Model):
    subjectname = models.CharField(max_length=50)
    subjectImage = models.ImageField(upload_to='subjectimages')



    def __str__(self):
        return self.subjectname
    #THIS CORRECT THE NAME REFRECTED ON ADMIN
    

    class Meta: #THIS PREVENT DEFAULT FROM ADDING S
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

    


class Course(models.Model):
    courseSubject = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='course', verbose_name='Course Subject')
    courseImage = models.ImageField(upload_to='subjectimages', help_text='image size should be below 10mb', verbose_name= 'Course Image')
    courseName  = models.CharField(max_length=100, verbose_name= 'Course Name')
    coursePrice = models.PositiveIntegerField(help_text='Enter Price in dollars', verbose_name= 'Course Price')
    courseDuration = models.DurationField(default=timedelta(hours=6, minutes=20), verbose_name=' Course Duration')


    def __str__(self):
        return self.courseName
    #THIS GIVE DEFINATE NAME TO YOUR MODEL NAME ON ADMIN
    