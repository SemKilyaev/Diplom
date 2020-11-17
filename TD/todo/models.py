from django.db import models
from django.contrib.auth.models import User

		
class Client(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE) # устанавливаем отношение 1 к 1 между клиентом и пользователем.
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


class Todo(models.Model):
	client = models.ForeignKey(Client, null=True, on_delete=models.CASCADE)
	text = models.CharField(max_length=40)
	complete = models.BooleanField(default=False)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.text