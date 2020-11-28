from django.db import models
from django.contrib.auth.models import User
import datetime

		
class Client(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE) # устанавливаем отношение 1 к 1 между клиентом и пользователем.
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


class Todo(models.Model):
	STATUS = (
		('Important', 'Important'),
		('Soon', 'Soon'),
	)

	client = models.ForeignKey(Client, null=True, on_delete=models.CASCADE)
	text = models.CharField(max_length=200, null=True)
	complete = models.BooleanField(default=False)
	date_created = models.DateTimeField(auto_now_add=True)
	make_up = models.DateField(null=True)
	date_completed = models.BooleanField(default=False)
	status = models.CharField(max_length=200, null=True)

	class Meta:
		ordering = ["-date_created"]

	def __str__(self):
		return self.text

