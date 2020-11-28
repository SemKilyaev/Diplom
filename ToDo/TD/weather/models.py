from django.db import models
from todo.models import Client
class City(models.Model):
	name = models.CharField(max_length = 30)
	client = models.ForeignKey(Client, null=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.name