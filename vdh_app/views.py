from django.shortcuts import render

from .models import Customer, CustomerInfo

# Create your views here.

def home(request):
	'''The home page for vDining Hall'''
	return render(request, 'vdh_app/home_page.html')

def all_customers(request):
	'''Retrieve all customers by name'''
	customers_all = Customer.objects.all() # all customers
	context = {'customers':customers_all }
	return render(request, 'vdh_app/all_customers.html', context)