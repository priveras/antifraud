from django.db import models

class Payment(models.Model):
	created_at = models.DateTimeField('created at')
	charge_id = models.CharField(max_length=200)
	amount = models.CharField(max_length=100)
	status = models.CharField(max_length=200)

	def __str__(self):
		return self.charge_id


