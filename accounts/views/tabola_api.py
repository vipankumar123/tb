from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.models import User


class ListingView(View):

    templates_name = 'apis/listing.html'

    def get(self,request):
        context = {}
        try:
            success_msg = self.request.GET.get('success_msg')
            msg = self.request.GET.get('msg')

            return render(request,self.templates_name,context)
        except Exception as e:
            print(e)
            context['msg'] = 'Something Went Wrong, Please Try Again or Contact Us'
            return render(request,self.templates_name,context)

           
