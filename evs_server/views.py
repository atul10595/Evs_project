from django.shortcuts import render

from django.http import HttpResponse,StreamingHttpResponse
from evs_server.models import *
from evs_server.models1 import *

from django.views.decorators.csrf import csrf_exempt

import json
import MySQLdb
db = MySQLdb.connect("localhost","root","mohit1995","CSV_SQL")

# prepare a cursor object using cursor() method
cursor = db.cursor()

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
	db = MySQLdb.connect("localhost","root","mohit1995","EVS")
	cursor = db.cursor()
	sql = "SELECT * FROM BUS_INSTANCE_TABLE;"
	cursor.execute(sql)
	data = cursor.fetchall()
	businstance_list = data
	sql = "SELECT * FROM evs_server_location;"
	cursor.execute(sql)
	data = cursor.fetchall()
	location_list = data
	sql = "SELECT * FROM evs_server_check1;"
	cursor.execute(sql)
	data = cursor.fetchall() 
	check_list = data
	db.close()

	location_list = EvsServerLocation.objects.all()
	#check_list = EvsServerCheck1.objects.all()
	#print location_list
	#print check_list
	#print businstance_list
	context={'location_list': location_list,'check_list':check_list,'businstance_list':businstance_list}
	return render(request, 'index.html', context)

@csrf_exempt
def src(request):
	if(request.method=='POST') :
		json_data = request.read()
		data = json.loads(json_data)
		Bus_no = data['bus_no']
		Latitude = data['latitude']
		Longitude = data['longitude']
		#loc = EvsServerLocation(bus_no= Bus_no, latitude=Latitude, longitude = Longitude)
		db = MySQLdb.connect("localhost","root","mohit1995","EVS")
		cursor = db.cursor()
		if int(Bus_no)<=9 :
			sql = "UPDATE BUS_INSTANCE_TABLE SET LATITUDE=%f,LONGITUDE=%f WHERE BUS_NO=%d" % (float(Latitude),float(Longitude),int(Bus_no))
			print sql
			try:
				cursor.execute(sql)
				db.commit()
			except:
				print "ERROR!!"
				db.rollback()
			db.close()
		#loc.save()
		print Latitude
		print Longitude
		return HttpResponse("Hello")
	return HttpResponse("Bie")

data1 = ""

@csrf_exempt
def user(request):
	if(request.method=='POST') :
		json_data = request.read()
		data = json.loads(json_data)
		Bus_no = data['bus_no']
		Latitude = data['latitude']
		Longitude = data['longitude']
		#loc = EvsServerLocation(bus_no= Bus_no, latitude=Latitude, longitude = Longitude)
		#loc.save()
		if(len(Bus_no) == 6) :
			db = MySQLdb.connect("localhost","root","mohit1995","EVS")
			cursor = db.cursor()
			sql = "SELECT LATITUDE,LONGITUDE FROM STOP_TABLE;"
			cursor.execute(sql)
			data = cursor.fetchall()
			bus_list = data
			pos=-1;
			k=0;
			min1 = 100.00
			min2 = 100.00
			for i in bus_list :
				if i[0]>float(Latitude) :
					diff1 = float(i[0])-float(Latitude)
				else :
				 	diff1 = float(Latitude)-float(i[0])
				if i[1]>float(Longitude) :
					diff2 = float(i[1])-float(Longitude)
				else :
					diff2 = float(Longitude) - float(i[1])	
				if(diff1<min1 and diff2<min2) :
					pos = k
					min1 = diff1
					min2 = diff2
				k+=1
			j = 0
			sql = "SELECT * FROM STOP_TABLE;"
			cursor.execute(sql)
			data = cursor.fetchall()
			bus_list = data
			for i in bus_list :
				if(j==pos) :
					data1 = i[0]
					break
				j+=1
			print data1
			value = Bus_no.split(" ")[1]
			loc = EvsServerLocation(bus_no= data1, latitude=float(value), longitude = 0.0)
			loc.save()
			db.close()
		else :
			db = MySQLdb.connect("localhost","root","mohit1995","EVS")
			cursor = db.cursor()
			sql = "SELECT LATITUDE,LONGITUDE FROM STOP_TABLE;"
			cursor.execute(sql)
			data = cursor.fetchall()
			bus_list = data
			pos=-1;
			k=0;
			min1 = 100.00
			min2 = 100.00
			for i in bus_list :
				if i[0]>float(Latitude) :
					diff1 = float(i[0])-float(Latitude)
				else :
				 	diff1 = float(Latitude)-float(i[0])
				if i[1]>float(Longitude) :
					diff2 = float(i[1])-float(Longitude)
				else :
					diff2 = float(Longitude) - float(i[1])	
				if(diff1<min1 and diff2<min2) :
					pos = k
					min1 = diff1
					min2 = diff2
				k+=1
			j = 0
			sql = "SELECT * FROM STOP_TABLE;"
			cursor.execute(sql)
			data = cursor.fetchall()
			bus_list = data
			for i in bus_list :
				if(j==pos) :
					data = i[0]
					break
				j+=1
			print data
			sql = "SELECT bus_no FROM evs_server_location WHERE latitude=%.1f AND longitude=0.0" %(float(Bus_no))
			print sql
			cursor.execute(sql)
			data2 = cursor.fetchall()
			for i in data2 :
				data3=i
				for j in data3 :
					data1 = j
					break
				break
			print data1
			sql = "SELECT * FROM BUS_INSTANCE_TABLE WHERE BUS_NO IN (SELECT * FROM (SELECT T1.BUS_NO FROM STOP_ROUTE_TABLE T1,STOP_ROUTE_TABLE T2 WHERE T1.BUS_STAND='%s' AND T2.BUS_STAND='%s' AND T1.BUS_NO=T2.BUS_NO) AS P)" %(data1,data)
			print sql
			cursor.execute(sql)
			data = cursor.fetchall()
			bus_list = data
			print data
			for i in data :
				loc = EvsServerLocation(bus_no=int(i[0]), latitude=i[1], longitude = i[2])
				loc.save()
			sql = "DELETE FROM evs_server_location WHERE latitude=%f AND longitude=0.0" %(float(Bus_no))
			try:
				cursor.execute(sql)
				db.commit()
			except:
				db.rollback()
				db.close() 
			db.close()
		print Latitude
		print Longitude
		return HttpResponse("Hello")
	return HttpResponse("Bie")

def getdata(request):
	if(request.method=='GET') :
		db = MySQLdb.connect("localhost","root","mohit1995","EVS")
		cursor = db.cursor()
		sql = "SELECT * FROM evs_server_location"
		cursor.execute(sql)
		data = cursor.fetchall()
		res = ""
		for i in data :
			res = res + i[1]+","+i[2]+","+i[3]+ ","
		print res
		sql = "DELETE FROM evs_server_location"
		try:
			cursor.execute(sql)
			db.commit()
		except:
			db.rollback()
			db.close() 
		db.close()
		print res
		return StreamingHttpResponse(res)
	return HttpResponse("Hell")