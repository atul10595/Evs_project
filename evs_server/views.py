from django.shortcuts import render

from django.http import HttpResponse,StreamingHttpResponse
from evs_server.models import *
from evs_server.models1 import *

from django.views.decorators.csrf import csrf_exempt

import json

@csrf_exempt
def index(request):
	if(request.method=='POST') :
		json_data = request.read()
		data = json.loads(json_data)
		Bus_no = data['bus_no']
		Latitude = data['latitude']
		Longitude = data['longitude']
		loc = EvsServerLocation(bus_no= Bus_no, latitude=Latitude, longitude = Longitude)
		loc.save()
	location_list = EvsServerLocation.objects.all()
	check_list = EvsServerCheck1.objects.all()
	print check_list
	context={'location_list': location_list,'check_list':check_list}
	return render(request, 'index.html', context)