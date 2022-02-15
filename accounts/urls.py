from django.urls import path
from .views import *

urlpatterns = [

		path('login/',LoginView.as_view(),name = 'LoginView'),
		path('',ListingView.as_view(),name = 'ListingView'),

]
