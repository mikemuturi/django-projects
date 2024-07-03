from django.db import models

# Create your models here.
genderInstance = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Any other', 'Any other')
)

class userInformation(models.Model):
    first_name = models.CharField(max_length=30)
    user_story = models.TextField(null=True, blank=True)
    profilePic = models.ImageField(upload_to='profile')
    DateofBirth = models.DateField()
    DateofRegistration = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=50)
    useResume = models.FileField(upload_to="cvs")
    salary = models.PositiveIntegerField()
    height = models.FloatField()
    gender = models.CharField(choices=genderInstance, max_length=30)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name
