from django.db import models


class Camping_level(models.Model):
	json_id = models.CharField(max_length = 100, null = True, blank = True)
	Campaign_Name = models.CharField(max_length=100, null=True, blank=True)
	Campaign_Status = models.CharField(max_length=100, null=True, blank=True)
	Taboola_Clicks = models.CharField(max_length=100, null=True, blank=True)
	Campaign_CTR = models.CharField(max_length=100, null=True, blank=True)
	Taboola_Campaign_Level_CPC = models.CharField(max_length=100, null=True, blank=True)
	Daily_Spend = models.CharField(max_length=100, null=True, blank=True)


class Analytics_API(models.Model):
	analytics_session = models.CharField(max_length=100, null=True, blank=True)
	AdSense_CPC = models.CharField(max_length=100, null=True, blank=True)
	AdSense_CTR = models.CharField(max_length=100, null=True, blank=True)
	AdSense_Campaign_level_revenue = models.CharField(max_length=100, null=True, blank=True)
	Total_Revenue = models.CharField(max_length=100, null=True, blank=True)
	RPM = models.CharField(max_length=100, null=True, blank=True)
	Coverage = models.CharField(max_length=100, null=True, blank=True)


class Campign_Site_Level(models.Model):
	Campaign_Name = models.CharField(max_length=100, null=True, blank=True)
	Taboola_Click = models.CharField(max_length=100, null=True, blank=True)
	Taboola_CPC = models.CharField(max_length=100, null=True, blank=True)
	CPC = models.CharField(max_length=100, null=True, blank=True)
	CTR = models.CharField(max_length=100, null=True, blank=True)
	Daily_Campain_Level_Site_Spend = models.CharField(max_length=100, null=True, blank=True)
	Campain_Site_Level_Bid_Changing = models.CharField(max_length=100, null=True, blank=True)
	Site_Block_Unblock_Capign_Level = models.CharField(max_length=100, null=True, blank=True)


class Google_Analytics_API(models.Model):
	Session = models.CharField(max_length=100, null=True, blank=True)
	AdSense_CPC = models.CharField(max_length=100, null=True, blank=True)
	CPC = models.CharField(max_length=100, null=True, blank=True)
	CTR = models.CharField(max_length=100, null=True, blank=True)
	Revenue = models.CharField(max_length=100, null=True, blank=True)
	Coverage = models.CharField(max_length=100, null=True, blank=True)
	Daily_Spend= models.CharField(max_length=100, null=True, blank=True)




