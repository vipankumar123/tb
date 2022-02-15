"""Hello Analytics Reporting API V4."""

import numpy as np
import pandas as pd
from google.oauth2 import service_account
from apiclient.discovery import build
from django.views.generic import View
from django.shortcuts import render

your_view_id = '240064866'
ga_keys = 'C:/Users/Hy_vipan/Documents/latestnithu-c2c2137f5384.json'


def format_summary(response):
    try:
        # create row index
        try: 
            row_index_names = response['reports'][0]['columnHeader']['dimensions']
            row_index = [ element['dimensions'] for element in response['reports'][0]['data']['rows'] ]
            row_index_named = pd.MultiIndex.from_arrays(np.transpose(np.array(row_index)), 
                                                        names = np.array(row_index_names))
        except:
            row_index_named = None
        
        # extract column names
        summary_column_names = [item['name'] for item in response['reports'][0]
                                ['columnHeader']['metricHeader']['metricHeaderEntries']]
    
        # extract table values
        summary_values = [element['metrics'][0]['values'] for element in response['reports'][0]['data']['rows']]
    
        # combine. I used type 'float' because default is object, and as far as I know, all values are numeric
        df = pd.DataFrame(data = np.array(summary_values), 
                          index = row_index_named, 
                          columns = summary_column_names).astype('float')
    
    except:
        df = pd.DataFrame()
        
    return df



def format_pivot(response):
    try:
        # extract table values
        pivot_values = [item['metrics'][0]['pivotValueRegions'][0]['values'] for item in response['reports'][0]
                        ['data']['rows']]
        
        # create column index
        top_header = [item['dimensionValues'] for item in response['reports'][0]
                      ['columnHeader']['metricHeader']['pivotHeaders'][0]['pivotHeaderEntries']]
        column_metrics = [item['metric']['name'] for item in response['reports'][0]
                          ['columnHeader']['metricHeader']['pivotHeaders'][0]['pivotHeaderEntries']]
        array = np.concatenate((np.array(top_header),
                                np.array(column_metrics).reshape((len(column_metrics),1))), 
                               axis = 1)
        column_index = pd.MultiIndex.from_arrays(np.transpose(array))
        
        # create row index
        try:
            row_index_names = response['reports'][0]['columnHeader']['dimensions']
            row_index = [ element['dimensions'] for element in response['reports'][0]['data']['rows'] ]
            row_index_named = pd.MultiIndex.from_arrays(np.transpose(np.array(row_index)), 
                                                        names = np.array(row_index_names))
        except: 
            row_index_named = None
        # combine into a dataframe
        df = pd.DataFrame(data = np.array(pivot_values), 
                          index = row_index_named, 
                          columns = column_index).astype('float')
    except:
        df = pd.DataFrame()
    return df



def format_report(response):
    summary = format_summary(response)
    pivot = format_pivot(response)
    if pivot.columns.nlevels == 2:
        summary.columns = [['']*len(summary.columns), summary.columns]
    
    return(pd.concat([summary, pivot], axis = 1))

def run_report(body, credentials_file):
    #Create service credentials
    credentials = service_account.Credentials.from_service_account_file(credentials_file, 
                                scopes = ['https://www.googleapis.com/auth/analytics.readonly'])
    #Create a service object
    service = build('analyticsreporting', 'v4', credentials=credentials)
    
    #Get GA data
    response = service.reports().batchGet(body=body).execute()
    
    return(format_report(response))


# ga_report = run_report(body, ga_keys)
# print("ga_report",ga_report)


# credentials = service_account.Credentials.from_service_account_file(ga_keys, 
#                                 scopes = ['https://www.googleapis.com/auth/analytics.readonly'])
# #Create a service object
# service = build('analyticsreporting', 'v4', credentials=credentials)
    
# #Get GA data
# response = service.reports().batchGet(body=body).execute()
# print("response",response)

# format_pivot(response)



# top_header = [item['dimensionValues'] for item in response['reports'][0]
#                       ['columnHeader']['metricHeader']['pivotHeaders'][0]['pivotHeaderEntries']]
# column_metrics = [item['metric']['name'] for item in response['reports'][0]
#                           ['columnHeader']['metricHeader']['pivotHeaders'][0]['pivotHeaderEntries']]
# array = np.concatenate((np.array(top_header),
#                         np.array(column_metrics).reshape((len(column_metrics),1))),
#                        axis = 1)
# column_index = pd.MultiIndex.from_arrays(np.transpose(array))
# print(column_index)


# x = [item.get('dimensionValues') for item in response['reports'][0]['columnHeader']['metricHeader']['pivotHeaders'][0]['pivotHeaderEntries']]
# print("x", x)



# body = {'reportRequests': [{'viewId': your_view_id, 
#                             'dateRanges': [{'startDate': '2021-01-01', 'endDate': '2021-04-30'}],
#                             'metrics': [{'expression': 'ga:users'}], 
#                             'dimensions': [{'name': 'ga:yearMonth'}],
#                             "pivots": [{"dimensions": [{"name": "ga:channelGrouping"}],
#                                         "metrics": [{"expression": "ga:users"},
#                                                     {"expression": "ga:bounceRate"}]
#                                        }]
#                           }]}


# report = run_report(body, ga_keys)
# print("report", report)






class GoogleAnalyticsList(View):

    templates_name = 'google/google_analytic.html'

    def get(self,request):
        context = {}
        try:
            success_msg = self.request.GET.get('success_msg')
            msg = self.request.GET.get('msg')
            all_records = Camping_level.objects.all().order_by('-id') 
            context['all_records'] = all_records

            return render(request,self.templates_name,context)

        except Exception as e:
            print(e)
            print('\n'*3)
            context['msg'] = 'Something Went Wrong, Please Try Again or Contact Us'
            return render(request,self.templates_name,context)
