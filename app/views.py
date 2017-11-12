from flask import render_template, request,flash, redirect, url_for,session
from app import app, db
from app.models import *
import datetime 
import os,time
from itertools import cycle
from app.models import *
import requests
import json
@app.route('/')
def index():
	return render_template('home.html')
@app.route('/hospital' )
def sama():
	return render_template('hospital.html')
@app.route('/ambulance')
def kchbhi():
	return render_template('ambulance.html')
@app.route('/ambulances')
def ambu():
	return render_template('ap_ambulance.html')
@app.route('/notifications')
def notify():
	return render_template('notification.html')
@app.route('/person', methods=['POST'])
def person():
	data = [{'name' : 'Anmol Mahajan', 'Age':20,'date' : '28/08/2017','hosp' : 'Indra Gandhi Medical College','HB' : '11gm','SugarBM' : '100', 'SugarAM' : '150', 'Uric' : '5', 'cholestrol' : '330', 'BP' : '110/150', 'issue' : 'Increased Blood Pressure'},{'name' : 'Anmol Mahajan', 'Age':20,'date' : '28/02/2017','hosp' : 'Tenzin Hospital','HB' : '10.6gm','SugarBM' : '100', 'SugarAM' : '190', 'Uric' : '5', 'cholestrol' : '310', 'BP' : '120/180', 'issue' : 'Increased Blood Pressure and Cholestrol'},{'name' : 'Anmol Mahajan', 'Age':20,'date' : '28/08/2017','hosp' : 'Indra Gandhi Medical College','HB' : '11gm','SugarBM' : '100', 'SugarAM' : '150', 'Uric' : '5', 'cholestrol' : '330', 'BP' : '110/150', 'issue' : 'Increased Blood Pressure'},{'name' : 'Anmol Mahajan', 'Age':20,'date' : '28/04/2017','hosp' : 'Tenzin Hospital','HB' : '11.6gm','SugarBM' : '120', 'SugarAM' : '190', 'Uric' : '5', 'cholestrol' : '310', 'BP' : '120/180', 'issue' : 'Increased Blood Pressure and Cholestrol'},{'name' : 'Anmol Mahajan', 'Age':20,'date' : '28/08/2017','hosp' : 'Indra Gandhi Medical College','HB' : '11gm','SugarBM' : '100', 'SugarAM' : '150', 'Uric' : '5', 'cholestrol' : '330', 'BP' : '110/150', 'issue' : 'Increased Blood Pressure'},{'name' : 'Anmol Mahajan', 'Age':20,'date' : '28/04/2017','hosp' : 'Tenzin Hospital','HB' : '11.6gm','SugarBM' : '120', 'SugarAM' : '190', 'Uric' : '5', 'cholestrol' : '310', 'BP' : '120/180', 'issue' : 'Increased Blood Pressure and Cholestrol'},{'name' : 'Anmol Mahajan', 'Age':20,'date' : '28/08/2017','hosp' : 'Indra Gandhi Medical College','HB' : '11gm','SugarBM' : '100', 'SugarAM' : '150', 'Uric' : '5', 'cholestrol' : '330', 'BP' : '110/150', 'issue' : 'Increased Blood Pressure'},{'name' : 'Anmol Mahajan', 'Age':20,'date' : '28/04/2017','hosp' : 'Tenzin Hospital','HB' : '11.6gm','SugarBM' : '120', 'SugarAM' : '190', 'Uric' : '5', 'cholestrol' : '310', 'BP' : '120/180', 'issue' : 'Increased Blood Pressure and Cholestrol'}]
	return render_template('not.html',data=data)
@app.route('/adhar')
def adhar():
	return render_template('adhar.html')

@app.route('/report')
def report():
	a = Person('946925494648','Anmol Mahajan',20,'Male','8627928036')
	db.session.add(a)
	a = Person('946925494647','Himank Jog',20,'Male','8628821312')
	db.session.add(a)
	a = Person('946925494646','Saksham Thakur',21,'Male','7018941670')
	db.session.add(a)
	a = Person('946925494645','Nikhil Sharma',20,'Male','8988038211')
	db.session.add(a)
	a = Person('946925494644','Anshul Chauhan',20,'Male','8629010465')
	db.session.add(a)
	a = Person('946925494643','Dhruv Dhingra',20,'Male','9650600245')
	db.session.add(a)
	b = Report('946925494648','28/08/2017','Indra Gandhi Medical College','11gm','100','150','5','240','90/130','Fever')
	db.session.add(b)
	b = Report('946925494648','29/08/2017','Indra Gandhi Medical College','11gm','100','150','5','240','80/120','Ulsers')
	db.session.add(b)
	b = Report('946925494645','28/09/2017','Tenzin Hospital','13gm','120','180','5','230','80/110','Vomitting')
	db.session.add(b)
	db.session.commit()
	return "sexo"
@app.route('/add' )
def sam():
	a=Hospitals("Dispensary Shoghi",31.1048 ,77.1712,"shoghi@gmail.com")
	db.session.add(a)
	a=Hospitals("Dispensary Tara Devi",31.1048,77.1734,"tare_devi@gmail.com") 
	db.session.add(a)
	a=Hospitals("Indira Gandhi Medical College Shimla",31.1071, 77.1831,"igmc@gmail.com")
	db.session.add(a)
	a=Hospitals("Indus Shimla",31.1048,77.1734,"indus@gmail.com")
	db.session.add(a)
	a=Hospitals("Lady Reading Shimla",31.1048,77.1714,"lady_reading@gmail.com")
	db.session.add(a)
	a=Hospitals("Tenzin Hospital",31.0729,77.1816,"tenzin@gmail.com")
	db.session.add(a)
	a=Hospitals("Postgraduate Institute of Medical Education and Research",30.7645, 76.7764,"Pgi@gmail.com")
	db.session.add(a)
	db.session.commit()
	igmc=Hospitals.query.filter_by(name='Indira Gandhi Medical College Shimla').first()
	tenzin=Hospitals.query.filter_by(name='Tenzin Hospital').first()
	pgi=Hospitals.query.filter_by(name='Postgraduate Institute of Medical Education and Research').first()
	a=Doctors("Anmol Mahajan","Internal Injury","Yes",pgi,"12345")
	b=Equipment("Cell processors","Internal Injury",pgi,.21)
	c=Equipment("Blood Salvage Machines","Internal Injury",pgi,.26)
	db.session.add(a)
	db.session.add(b)
	db.session.add(c)
	a=Doctors("Akhil Mittal","Internal Injury","Yes",igmc,"230124")
	b=Equipment("Cell processors","Internal Injury",igmc,.21)
	c=Equipment("Blood Salvage Machines","Internal Injury",igmc,.26)
	db.session.add(a)
	db.session.add(b)
	db.session.add(c)
	a=Doctors("Pritish Mukherjee","Internal Injury","Yes",tenzin,"230120")
	b=Equipment("Cell processors","Internal Injury",tenzin,.21)
	c=Equipment("Blood Salvage Machines","Internal Injury",tenzin,.26)
	db.session.add(a)
	db.session.add(b)
	db.session.add(c)
	a=Internal_Injury("Tenzin Hospital",50,10);	
	b=Internal_Injury("Indira Gandhi Medical College Shimla",30,3);
	c=Internal_Injury("Postgraduate Institute of Medical Education and Research",80,8);
	db.session.add(a)
	db.session.add(b)
	db.session.add(c)
	a=Burns("Tenzin Hospital",30,3);	
	b=Burns("Indira Gandhi Medical College Shimla",50,10);
	db.session.add(a)
	db.session.add(b)
	a=Doctors("Ashutosh Sharma","Brain Injury","Yes",pgi,"31024")
	b=Equipment("Ventilator","Brain Injury",pgi,.09)
	c=Equipment("Foley Catheter","Brain Injury",pgi,.27)
	d=Equipment("Nasogastric Tube","Brain Injury",pgi,.12)
	e=Equipment("EKG Machine","Brain Injury",pgi,.26)
	f=Equipment("Pulse Oximeter","Brain Injury",pgi,.23)
	db.session.add(a)
	db.session.add(b)
	db.session.add(c)
	db.session.add(d)
	db.session.add(e)
	db.session.add(f)
	a=Doctors("Akhil Sahota","Brain Injury","Yes",tenzin,"230126")
	db.session.add(a)
	b=Equipment("Ventilator","Brain Injury",igmc,.09)
	c=Equipment("Foley Catheter","Brain Injury",igmc,.27)
	d=Equipment("Nasogastric Tube","Brain Injury",igmc,.12)
	e=Equipment("EKG Machine","Brain Injury",igmc,.26)
	f=Equipment("Pulse Oximeter","Brain Injury",igmc,.23)
	db.session.add(b)
	db.session.add(c)
	db.session.add(d)
	db.session.add(e)
	db.session.add(f)
	a=Brain("Tenzin Hospital",20,10);	
	b=Brain("Postgraduate Institute of Medical Education and Research",50,42);
	db.session.add(a)
	db.session.add(b)
	a=Doctors("Sahil Ratra","Burns","Yes",pgi,"230120")#burns find nearby asap
	b=Equipment("Vivascope","Burns",pgi,.32)
	c=Equipment("Virtual Pain Relief Machine","Burns",pgi,.20)
	d=Equipment("Hyaluronic acid based dressing","Burns",pgi,.24)
	e=Equipment("Dermatone","Burns",pgi,.25)
	db.session.add(a)
	db.session.add(b)
	db.session.add(c)
	db.session.add(d)
	db.session.add(e)
	a=Doctors("Sahil Shama","Burns","Yes",tenzin,"230122")#burns find nearby asap
	b=Equipment("Dermatone","Burns",tenzin,.25)
	db.session.add(a)
	db.session.add(b)
	a=Doctors("Sahil Thakur","Burns","Yes",igmc,"230112")
	b=Equipment("Vivascope","Burns",igmc,.32)
	a=Burns("Tenzin Hospital",1,5);	
	b=Burns("Postgraduate Institute of Medical Education and Research",5,20);
	db.session.add(a)
	db.session.add(b)
	a=Burns("Indira Gandhi Medical College Shimla",1,5);	
	db.session.commit()
	return "success"	
@app.route("/sa",methods=["GET","POST"])	
def la():
	loc=request.form["name"]
	return render_template('scriptsss.html',c=loc)	

@app.route('/internal_injury')
def intern():
	A=set()
	B=set()
	k=0
	c=Hospitals.query.all()
	for i in c:
		for j in i.doctors:
			if(j.specialisation=="Internal Injury" and j.availability=="Yes"):
				A.add(i)
				break
	for i in c:
		k=0
		for j in i.equipments:
			if(j.name=="Cell processors" or j.name=="Blood Salvage Machines"):
				k+=1
			if(k==2):	
				B.add(i)
				break
	C=A.intersection(B)
	for i in C:
		##print i.name
	# send_url = 'http://freegeoip.net/json'
	# r = requests.get(send_url)
	# j = json.loads(r.text)
	# lat = j['latitude']
	# lon = j['longitude']
	# d=[lat,lon]	

	#will be sorted by factors like(distance,rush ,proficiency offered by equipment and seriousness of case)etc. ->will together add up to give us a factor->which is chances of survival 		
	#in case is very_serious and distance is more then choose the hospital , so that some initial treatment for stabalisation of his conditaion can be done->normalistaion of distance and equipments only
	return render_template('internal.html')						
	#Let formula be :  (registered/capacity+distance)
@app.route('/br')
def lol():
	A=set()
	B=set()
	k=0
	c=Hospitals.query.all()
	for i in c:
		for j in i.doctors:
			if(j.specialisation=="Internal Injury" and j.availability=="Yes"):
				A.add(i)
				break
	for i in c:
		k=0
		for j in i.equipments:
			if(j.name=="Cell processors" or j.name=="Blood Salvage Machines"):
				k+=1
			if(k==2):	
				B.add(i)
				break
	C=["Indira Gandhi Medical College Shimla","Tenzin Hospital","Postgraduate Institute of Medical Education and Research"]
	d=[]
	for i in C:
		#print i
		e=Internal_Injury.query.filter_by(hos_name=i).first()
		d.append(float(e.registered)/float(e.capacity))
	return render_template('index.html',c=["Indira Gandhi Medical College Shimla","Tenzin Hospital","Postgraduate Institute of Medical Education and Research"],d=d)

@app.route('/brain')
def brain():
	A=set()
	B=set()
	k=0
	c=Hospitals.query.all()
	for i in c:
		for j in i.doctors:
			if(j.specialisation=="Brain Injury" and j.availability=="Yes"):
				A.add(i)
				break
	for i in c:
		k=0
		for j in i.equipments:
			if(j.name=="Ventilator" or j.name=="Foley Catheter" or j.name=="Nasogastric Tube"  or j.name=="EKG Machine" or j.name=="Pulse Oximeter"):
				k+=1
			if(k==5):	
				B.add(i)
				break
	C=A.intersection(B)		
	#print C###only Postgraduate Institute of Medical Education and Research falls under this as it covers all of the requirements.So just display it and show its score is very less and provide a button (better logistics) which will then lead to a combination for tenzin and igmc. Display that all the required instruments and the doctor are available. 
	return render_template("scriptsss2.html",c = next(iter(C)))

@app.route('/brain2')
def brain2():
	return render_template("left.html")#display that there is a combination for nearby hospitals that can be better
@app.route('/brain3')
def brain3():
	return render_template('scriptsss.html',c="Indira Gandhi Medical College Shimla")
@app.route('/burns')
def burns():
	A=set()
	B=set()
	k=0
	c=Hospitals.query.all()
	for i in c:
		for j in i.doctors:
			if(j.specialisation=="Burns" and j.availability=="Yes"):
				A.add(i)
				break
	for i in c:
		k=0
		for j in i.equipments:
			if(j.name=="Vivascope" or j.name=="Virtual Pain Relief Machine" or j.name=="Hyaluronic acid based dressing"  or j.name=="EKG Machine" or j.name=="Dermatone"):
				k+=1
			if(k==4):	
				B.add(i)
				break
	C=A.intersection(B)		
	#print C###only Postgraduate Institute of Medical Education and Research falls under this category.Show a button for alternate logistics and this time no  hospital.So check hoptitals by increasing radius distance turnwise and cover a hospital.->>rate the remaining  proficiency will be important
	return render_template("logis.html")

#Front end----Notification Portal for the hospital,Location share of ambulance for the hospital,mail or message to the concerning doctor.
@app.route('/burn2',methods=['GET','POST'])
def burn2():
	return render_template('scriptsss.html',c="Tenzin Hospital")
@app.route('/burn3')
def lolo():
	a=Hospitals.query.filter_by(name="Tenzin Hospital").first()
	k= a.equipments
	p=[]
	p1=0.0
	p2=0.0
	for i in k:
		if(i.dis_type=="Burns"):
			p1+=i.ind_prof;
	b=Hospitals.query.filter_by(name="Indira Gandhi Medical College Shimla").first()
	m=b.equipments
	for i in m:
		if(i.dis_type=="Burns"):
			p2+=i.ind_prof;
	p.append(p1)
	p.append(p2)
	#print p1,p2		
	e=Burns.query.filter_by(hos_name="Tenzin Hospital").first()
	f=Burns.query.filter_by(hos_name="Indira Gandhi Medical College Shimla").first()
	ru=[]
	ru.append(float(e.registered)/float(e.capacity))
	ru.append(float(f.registered)/float(f.capacity))
	f=["Indira Gandhi Medical College Shimla","Tenzin Hospital"]
	return render_template("map.html",ru=ru,p=p,c=f)