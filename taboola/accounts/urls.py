from django.urls import path
from .views import *

urlpatterns = [

		path('login/',LoginView.as_view(),name = 'LoginView'),
		path('LogoutView/',LogoutView.as_view(),name = 'LogoutView'),
		path('',ListingView.as_view(),name = 'ListingView'),
		path('edit/<int:id>/',EditView.as_view(),name = 'EditView'),
		path('hittingapi/',HittingAPI.as_view(),name = 'HittingAPI'),
		path('google_analytics/',GoogleAnalyticsList.as_view(),name = 'GoogleAnalyticsList'),

]
