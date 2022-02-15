from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.models import User

from accounts.models import Camping_level
import requests,json
from django.db.models import Q





def AccessToken(client_id,client_secret):
    try:
        url = "https://backstage.taboola.com/backstage/oauth/token"
        payload = "client_id={}&client_secret={}&grant_type=client_credentials".format(client_id,client_secret)
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.request("POST", url, data=payload, headers=headers)
        json_response = response.json()
        print("\n" * 3)
        return json_response.get('access_token')
    except Exception as e:
        return None



def getaccountId(token):
    try:
        url = "https://backstage.taboola.com/backstage/api/1.0/users/current/account"
        headers = {"Authorization": "Bearer {}".format(token)}
        response = requests.request("GET", url,headers=headers)
        account_json_response = response.json()
        accountId = account_json_response.get('account_id') 

        return accountId

    except:
        return None



class ListingView(View):

    templates_name = 'apis/listing.html'

    def get(self,request):
        context = {}
        try:
            all_records = Camping_level.objects.filter(Q(Campaign_Status = 'Running')|Q(Campaign_Status = 'PAUSED')) 
            print('59')
            print(all_records)
            context={'all_records' : all_records}
            success_msg = self.request.GET.get('success_msg')
            msg = self.request.GET.get('msg')

            return render(request,self.templates_name,context)

        except Exception as e:
            print(e)
            print('\n'*3)
            context['msg'] = 'Something Went Wrong, Please Try Again or Contact Us'
            return render(request,self.templates_name,context)


class EditView(View):

    templates_name = 'apis/edit.html'

    def get(self,request,id):
        context = {}
        try:
            one_record = Camping_level.objects.get(id = id)
            context['one_record'] = one_record
            return render(request,self.templates_name,context)
        except Exception as e:
            print(e)
            context['msg'] = 'Something Went Wrong, Please Try Again or Contact Us'
            return render(request,self.templates_name,context)

    def post(self,request,id):

        context={}
        try:
            one_record = Camping_level.objects.get(id = id)
            context['one_record'] = one_record

            name = request.POST.get('name')
            if not name:
                context['msg'] = ' Validation Error ! Please Enter Your name '
                return render(request,self.templates_name,context)

            Campaign_Status = request.POST.get('Campaign_Status')
            if not Campaign_Status:
                context['msg'] = ' Validation Error ! Please Enter Your Campaign_Status '
                return render(request,self.templates_name,context)

            Taboola_Clicks = request.POST.get('Taboola_Clicks')
            if not Taboola_Clicks:
                context['msg'] = ' Validation Error ! Please Enter Your Taboola_Clicks '
                return render(request,self.templates_name,context)

            Campaign_CTR = request.POST.get('Campaign_CTR')
            if not Campaign_CTR:
                context['msg'] = ' Validation Error ! Please Enter Your Campaign_CTR'
                return render(request,self.templates_name,context)

            Taboola_Campaign_Level_CPC = request.POST.get('Taboola_Campaign_Level_CPC')
            if not Taboola_Campaign_Level_CPC:
                context['msg'] = ' Validation Error ! Please Enter Your Taboola_Campaign_Level_CPC '
                return render(request,self.templates_name,context)

            Daily_Spend = request.POST.get('Daily_Spend')
            if not Daily_Spend:
                context['msg'] = ' Validation Error ! Please Enter Your Daily_Spend'
                return render(request,self.templates_name,context)

            Camping_level.objects.filter(id = id).update(Campaign_Name = name, Campaign_Status=Campaign_Status, Taboola_Clicks=Taboola_Clicks, Campaign_CTR=Campaign_CTR, Taboola_Campaign_Level_CPC=Taboola_Campaign_Level_CPC, Daily_Spend=Daily_Spend)




            one_record = Camping_level.objects.get(id = id)
            context['one_record'] = one_record




            url = "https://backstage.taboola.com/backstage/api/1.0/account_id/campaigns/campaign_id"
            payload = {"name": "DemoCampaign - Edited"}
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json"
            }

            response = requests.request("POST", url, json=payload, headers=headers)

            context['success_msg']='Success ! An record has been successfully updated into our database'
            return render(request,self.templates_name,context)
        except Exception as e:
            print(e)
            print('\n'*3)
            context['msg'] = 'Something Went Wrong, Please Try Again or Contact Us'
            return render(request,self.templates_name,context)   

class HittingAPI(View):

    templates_name = 'apis/listing.html'

    def get(self,request):
        context = {}
        try:



            client_id = '1b950ac73a1b49adb47542dfbde9eee7'
            client_secret = 'fe3f020b3b3b45ec911a1238e13f302b'

            refresh_token = AccessToken(client_id, client_secret)
            accountId = getaccountId(refresh_token)


            url = "https://backstage.taboola.com/backstage/api/1.0/{}/campaigns/".format(accountId)
            querystring = {"fetch_level":"R"}
            headers = {"Authorization": "Bearer {}".format(refresh_token),'Content-Type' : 'application/json'}
            response = requests.request("GET", url, headers=headers, params=querystring)
            print("\n" * 3)

            json_getting = response.json()
            checking_comping_level = Camping_level.objects.all().delete()

            for one in json_getting.get('results'):

                print(one)
                name = one.get('name')
                Campaign_Status = one.get('status')
                Taboola_Clicks = one.get('clicks')
                Campaign_CTR = one.get('ctr')
                Taboola_Campaign_Level_CPC = one.get('cpc')
                Daily_Spend = one.get('spent')

                json_id = one.get('id')

                print(json_id, name)

                checking_comping_level = Camping_level.objects.filter(json_id = json_id)
                if not checking_comping_level:
                    Camping_level.objects.create(json_id = json_id,Campaign_Name = name,Campaign_Status=Campaign_Status, Taboola_Clicks=Taboola_Clicks, Campaign_CTR=Campaign_CTR, Taboola_Campaign_Level_CPC=Taboola_Campaign_Level_CPC, Daily_Spend=Daily_Spend)






            return redirect('/?msg=Success ! New record has been added into our database')
        except Exception as e:
            print(e)
            context['msg'] = 'Something Went Wrong, Please Try Again or Contact Us'
            return render(request,self.templates_name,context)

    

