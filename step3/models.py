from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Name_Entity(models.Model):
	PERSON = 'Person'
	LOCATION = 'Location'
	ORGANIZATION = 'Organization'
	MONEY = 'Money'
	MISC = 'Misc'
	PHONE = 'Phone'
	INTERESTING = 'Interesting'
	DATE = 'Date'

	CATEGORY_CHOICES = (
		(PERSON, 'Person'),
		(LOCATION, 'Location'),
		(ORGANIZATION, 'Organization'),
		(MONEY, 'Money'),
		(MISC, 'Misc'),
		(PHONE, 'Phone'),
		(INTERESTING, 'Interesting'),
		(DATE, 'Date'),
		)

	entity_name = models.CharField(max_length=100, primary_key=True)
	entity_category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
#	friends = models.ManyToManyField('self', through="Relationship", symmetrical=False)
	# has many-to-many relationship with Document

	def __str__(self):
		return self.entity_name

class Document(models.Model):
	docID = models.CharField(max_length=20, primary_key=True) # the id of documents from sources, not primary key
	docDate = models.DateField(auto_now=False, auto_now_add=False, null=True)
	docSource = models.CharField(max_length=20, null=True)
	docText = models.TextField()
#	name_entities = models.ManyToManyField(Name_Entity, through="Membership")
	# has many-to-one relationship with ContextSlice

	def __str__(self):
		return self.doc_id

class Context_Slice(models.Model):
	NAME = 'NE'
	FREQ = 'RK'
	AJMC = 'CL'
	AJMF = 'FR'

	SLICE_CHOICE = (
		(NAME, 'certain name entities'),
		(FREQ, 'rank entities by their freqencies'),
		(AJMC, 'adjacency matrix of documents that are close - share many name entities'),
		(AJMF, 'adjacency matrix of documents that are far - share few name entities')
		)

	user_ID = models.AutoField(primary_key=True)
	slice_method = models.CharField(max_length=2, choices=SLICE_CHOICE, default=NAME)
	documents = models.ForeignKey(Document)
	# has one-to-one relationship with User

class User(models.Model):
	user_ID = models.AutoField(primary_key=True)
	login = models.DateTimeField(auto_now=False, auto_now_add=False)
	logout = models.DateTimeField(auto_now=False, auto_now_add=False)
	context_slice = models.OneToOneField(Context_Slice, on_delete=models.PROTECT)
	# has many-to-one relationship with Relationship

#intermediate model
#class Membership(models.Model):
#	document = models.ForeignKey(Document);
#	name_entities = models.ForeignKey(Name_Entity);

#intermediate model
class Friends(models.Model):
	NOT = 1
	LTL = 2
	AVG = 3
	VRY = 4
	ABS = 5

	IMPORTANCE_CHOICE = (
		(NOT, 'Not Important At All'),
		(LTL, 'Of Little Importance'),
		(AVG, 'Of Average Importance'),
		(VRY, 'Very Important'),
		(ABS, 'Absolutely Important'),
		)

	entity_ID = models.ForeignKey(Name_Entity, on_delete=models.PROTECT, related_name="entity_ID") #by user
	friend_with = models.ForeignKey(Name_Entity, on_delete=models.PROTECT, related_name="friend_with") #by user
	description = models.CharField(max_length=200) #by user
	importance = models.DecimalField(max_digits=1, decimal_places=0, choices=IMPORTANCE_CHOICE, default=AVG) #by user
	creator = models.ForeignKey(User, on_delete=models.PROTECT)
	time_stamp = models.DateTimeField(auto_now=False, auto_now_add=False)
	
	class Meta:
		unique_together = (("entity_ID","friend_with"),)

class Document_Entity(models.Model):
	pair_id = models.CharField(max_length=120, primary_key=True)
	document = models.ForeignKey(Document)
	entity = models.ForeignKey(Name_Entity)
	occurence = models.IntegerField(default=0)