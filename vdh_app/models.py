from django.db import models

# Create your models here.

class Customer(models.Model):
	'''Customer name.'''
	customer_name = models.CharField(max_length=50)
	date_joined = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		'''Return a string representation of customer name.'''
		return self.customer_name


class CustomerInfo(models.Model):
	"""Customer Info"""
	name = models.ForeignKey(Customer, on_delete=models.CASCADE) # connects each entry to a specific topic
	room_number = models.SmallIntegerField()
	phone_number = models.CharField(max_length=10) # put proper phone number field
	meal_plan = models.CharField(max_length=10) # put predefined meal plans here.
	#cancelled_meal = models.BooleanField()

	class Meta:
		verbose_name_plural = 'CustomersInfo'  # use CustomersInfo when refering to info of many customers

	def __str__(self):
		'''Return a string representation if the customer Info.'''
		return '%s, %s, %s'%(self.room_number, self.phone_number, self.meal_plan) # ok for now
		