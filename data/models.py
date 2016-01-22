from django.db import models

class Payment(models.Model):
	created_at = models.DateTimeField('created at')
	amount = models.CharField(max_length=100)
	status = models.CharField(max_length=200)

