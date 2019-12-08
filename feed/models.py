from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class UserProfile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,)
	photo = models.FileField()
	phone_no = models.IntegerField()
	status = models.CharField(max_length=1000)

	def ___str__(self):
		return self.phone_no

class Post(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	pic = models.FileField()
	quote = models.CharField(max_length=3000)
	likes = models.IntegerField(default=0)

	def ___str__(self):
		return self.pk

class Friend(models.Model):
	name = models.CharField(max_length=300)
	user = models.ManyToManyField(User)

	def ___str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('friends',args=[str(self.id)])