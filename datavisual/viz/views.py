# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db import models
from django.http import HttpResponse, StreamingHttpResponse
from django.template import loader
import psycopg2
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Enterpise_Data
from .forms import TableForm
import csv

# Create your views here.
#this is the view used for the data.html page

def index(request):
	
	ent_table = Enterpise_Data.objects.all().last().tables
	conn = psycopg2.connect("dbname='foursquare' user='foursquare' host='redshift.prod.foursquare.com' password='Dodgeball171' port=5439")
	cur = conn.cursor()

	#Will adjust this to just show a full basic set, full basic/premium set, full basic/premium set once I get this freaking data in redshift	
	#I would also like to add a variable to filter off country or state. May also be useful to add a filter for row limit too.

	if ent_table == 'enterpirse_data.venues_rich':
		cur.execute("""SELECT venueid, rating, price
						from enterprise_data.venues_rich
						LIMIT 10""")
		z = cur.fetchall()
		headers = ['venueid', 'rating', 'price']
		
	else:
		z = ent_table	
	

	context = {
		'z': z
	}	
	context_object_name = 'data_table'
	template = loader.get_template('index/data.html')
	return HttpResponse(template.render(context, request))


#below is used for the values.html page


def data_counts(request):
	
	conn = psycopg2.connect("dbname='foursquare' user='foursquare' host='redshift.prod.foursquare.com' password='Dodgeball171' port=5439")
	cur = conn.cursor()
	cur.execute("""SELECT sum(case when price <> '' or price IS NOT NULL THEN 1 ELSE 0 END) as price_counts

					FROM enterprise_data.venues_rich""")
	x = cur.fetchone()
	val = x[0]

''' Will use below once I get basic data in redshift. I would also like to add an option to cut this by country, or state, or category


	cur2 = conn.cursor()
	cur2.execute("""SELECT sum(case when address <> '' or address IS NOT NULL THEN 1 ELSE 0 END) as has_address,
						  sum(case when city <> '' or city IS NOT NULL THEN 1 ELSE 0 END) as has_city,
						  sum(case when dma <> '' or dma IS NOT NULL THEN 1 ELSE 0 END) as has_dma,
						  sum(case when state <> '' or state IS NOT NULL THEN 1 ELSE 0 END) as has_state,
						  sum(case when postalcode <> '' or postalcode IS NOT NULL THEN 1 ELSE 0 END) as has_zip,
						  sum(case when hours <> '' or price IS NOT NULL THEN 1 ELSE 0 END) as has_hours
					FROM enterprise_data.venues_basic""")
	x2 = cur.fetchall()
	val2 = x[0]'''

	context = {
		'val': val
		#'val2': val
	}
	
	template = loader.get_template('index/values.html')
	return HttpResponse(template.render(context, request))

# This class is for the dropdown

class DataCreateView(CreateView):
	model = Enterpise_Data
	form_class = TableForm
	template_name = 'index/selector.html'
	success_url = reverse_lazy('create_table')


# Want to provide a link to output a csv for the basic or basic/premium or basic/premium/rich - this part is very uncomplete
def data_download(request):

	#items = 
	response = HttpResponse(content_type = 'text/csv')
	response['Content-Disposition'] = 'attachment; filename="madata.csv"'

	writer = csv.writer(response, delimiter= ',')

