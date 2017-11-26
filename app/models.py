from app import db
from app import bcrypt
import datetime

class Hospitals(db.Model):
	__tablename__ = "Hospitals"
	extend_existing=True 
	name = db.Column(db.String(100),primary_key=True)#email-id for each hospital
	longitude = db.Column(db.Float, nullable=False)#add Solan hospital for burns
	latitude = db.Column(db.Float, nullable=False)
	email=db.Column(db.String(100),nullable=False)
	doctors = db.relationship('Doctors', backref="in_a", cascade="all, delete-orphan",lazy='dynamic')
	equipments = db.relationship('Equipment', backref="of_a", cascade="all, delete-orphan",lazy='dynamic')
	def __init__ (self,name,longitude,latitude,email):
		self.name = name
		self.longitude =longitude
		self.latitude=latitude
		self.email=email


class Doctors(db.Model):
	__tablename__ = "Doctors"
	id = db.Column(db.Integer, primary_key=True,autoincrement=True)
	name = db.Column(db.String(100),nullable=False)
	specialisation = db.Column(db.String(100),nullable=False)
	availability=db.Column(db.String(100),nullable=False)
	hos_name=db.Column(db.String(100), db.ForeignKey('Hospitals.name'))#a phone_no column should also be added
	phone_no=db.Column(db.String(12),nullable=False)
	def __init__ (self,name,specialisation,availability,ho_name,phone_no):
		self.name = name
		self.specialisation =specialisation
		self.availability=availability
		self.in_a=ho_name
		self.phone_no=phone_no

class Equipment(db.Model):
	__tablename__ = "Equipment"
	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	name = db.Column(db.String(100),nullable=False)#a proficiency column should also be added
	dis_type=db.Column(db.String(100),nullable=False)
	ind_prof=db.Column(db.Float,nullable=False)
	hosi_name=db.Column(db.String(100), db.ForeignKey('Hospitals.name'))
	def __init__(self,name,dis_type,ho_name,prof):
		self.name=name
		self.dis_type=dis_type
		self.of_a=ho_name
		self.ind_prof=prof

class Internal_Injury(db.Model):
	__tablename__ = "Internal_Injury"
	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	hos_name = db.Column(db.String(100),nullable=False)
	capacity=db.Column(db.Integer,nullable=False)
	registered=db.Column(db.Integer, nullable=False)
	def __init__(self,hos_name,capacity,registered):
		self.hos_name=hos_name
		self.capacity=capacity
		self.registered=registered
class Brain(db.Model):
	__tablename__ = "Brain"
	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	hos_name = db.Column(db.String(100),nullable=False)
	capacity=db.Column(db.Integer,nullable=False)
	registered=db.Column(db.Integer, nullable=False)
	def __init__(self,hos_name,capacity,registered):
		self.hos_name=hos_name
		self.capacity=capacity
		self.registered=registered
class Burns(db.Model):
	__tablename__ = "Burns"
	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	hos_name = db.Column(db.String(100),nullable=False)
	capacity=db.Column(db.Integer,nullable=False)
	registered=db.Column(db.Integer, nullable=False)
	def __init__(self,hos_name,capacity,registered):
		self.hos_name=hos_name
		self.capacity=capacity
		self.registered=registered

class Person(db.Model):
	__tablename__ = "person"
	id = db.Column(db.String(12),primary_key=True)
	name = db.Column(db.String(50))
	age = db.Column(db.Integer)
	sex = db.Column(db.String(10))
	contact = db.Column(db.String(13))
	report = db.relationship('Report', backref='person', lazy=True)

	def __init__(self,i,n,a,s,c):
		self.id = i
		self.name = n
		self.age = a
		self.sex = s
		self.contact = c 
class Report(db.Model):
	__tablename__ = "report"
	rep_id = db.Column(db.Integer,primary_key=True)
	id = db.Column(db.String(12), db.ForeignKey('person.id'),nullable=False)
	date = db.Column(db.String(10))
	hospital = db.Column(db.String(100))
	HB = db.Column(db.String(10))
	SugarBM = db.Column(db.String(10))
	SugarAM = db.Column(db.String(10))
	Uric = db.Column(db.String(10))
	cholestrol = db.Column(db.String(10))
	BP = db.Column(db.String(7))
	issue = db.Column(db.String(100))

	def __init__(self,i,d,h,hos,sbm,sam,u,ch,bp,issue):
		self.id = i
		self.date = d
		self.hospital = h
		self.HB = hos
		self.SugarBM = sbm
		self.SugarAM = sam
		self.Uric = u
		self.cholestrol = ch
		self.BP = bp
		self.issue = issue