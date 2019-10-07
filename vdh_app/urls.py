'''Defines URL patterns for vdh_app'''


from django.urls import path
from . import views

urlpatterns = [
	# Home page
	path('', views.home, name = 'home_page'), # use 'home' to refer to this url in other sections of the code
	path('all_customers', views.all_customers, name = 'all_customers'),
	]