from django.db import models

# Create your models here.
class User(models.Model):
	GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
	Name = models.CharField(max_length=100, blank=False)
	Email = models.EmailField(blank=False)
	Phone = models.CharField(max_length=15, blank=False, null=True)
	Age = models.IntegerField(blank=True, null=True	)
	Gender = models.CharField(max_length=1,choices=GENDER_CHOICES, blank=True)

	def get_details_url(self):
		return f"/user/details/{self.id}/"