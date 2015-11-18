from django.contrib.auth.models import User
from django.contrib import admin
from django.db import models

# Create your models here.
class Professor(models.Model):
	COLLEGES = (
		('Arch', 	'Architecture'),
		('AnL', 	'Arts & Letters'),
		('Business', 	'College of Business'),
		('EG', 		'Engineering'),
		('Law',		'Law School'),
		('SMC',		'Saint Mary\'s'),
		('Science',	'Science'),
	)
	DEPARTMENTS = (
		('Accounting', 'Accounting'),
		('Administrative and Commercial Studies', 'Administrative and Commercial Studies'),
		('Aerospace & Mechanical Engineering', 'Aerospace & Mechanical Engineering'),
		('Airforce Aerospace Studies', 'Airforce Aerospace Studies'),
		('American Studies', 'American Studies'),
		('Anaesthesia & Perioperative Medicine', 'Anaesthesia & Perioperative Medicine'),
		('Anatomy and Cell Biology', 'Anatomy and Cell Biology'),
		('Anthropology', 'Anthropology'),
		('Anthropology', 'Anthropology'),
		('Applied Mathematics', 'Applied Mathematics'),
		('Arabic Language/Literature', 'Arabic Language/Literature'),
		('Architecture', 'Architecture'),
		('Art, Art History, & Design', 'Art, Art History, & Design'),
		('Arts & Letters Departments', 'Arts & Letters Departments'),
		('Biochemistry', 'Biochemistry'),
		('Biological Sciences', 'Biological Sciences'),
		('Biology', 'Biology'),
		('Business Administration', 'Business Administration'),
		('Chemical and Biochemical Engineering', 'Chemical and Biochemical Engineering'),
		('Chemical Engineering', 'Chemical Engineering'),
		('Chemistry', 'Chemistry'),
		('Chemistry & Biochemistry', 'Chemistry & Biochemistry'),
		('Civil and Environmental Engineering', 'Civil and Environmental Engineering'),
		('Civil Engineering', 'Civil Engineering'),
		('Classic Literature/Ancient History', 'Classic Literature/Ancient History'),
		('Classical Studies', 'Classical Studies'),
		('Clinical Neurological Sciences', 'Clinical Neurological Sciences'),
		('Communication Sciences and Disorders', 'Communication Sciences and Disorders'),
		('Computer Applications', 'Computer Applications'),
		('Computer Engineering', 'Computer Engineering'),
		('Computer Science', 'Computer Science'),
		('Dentistry', 'Dentistry'),
		('Diagnostic Radiology and Nuclear Medicine', 'Diagnostic Radiology and Nuclear Medicine'),
		('Dummy', 'Dummy'),
		('Earth Sciences', 'Earth Sciences'),
		('East Asian Languages & Literature', 'East Asian Languages & Literature'),
		('Economics', 'Economics'),
		('Economics', 'Economics'),
		('Electrical and Computer Engineering', 'Electrical and Computer Engineering'),
		('Electrical Engineering', 'Electrical Engineering'),
		('Engineering Departments', 'Engineering Departments'),
		('English', 'English'),
		('English', 'English'),
		('Epidemiology and Biostatistics', 'Epidemiology and Biostatistics'),
		('Faculty of Education', 'Faculty of Education'),
		('Family Medicine', 'Family Medicine'),
		('Film Studies', 'Film Studies'),
		('Film, Television, & Theatre', 'Film, Television, & Theatre'),
		('Finance & Business Economics', 'Finance & Business Economics'),
		('First Year Writing Program', 'First Year Writing Program'),
		('French', 'French'),
		('French', 'French'),
		('Gender Studies', 'Gender Studies'),
		('Geography', 'Geography'),
		('German Language & Literature', 'German Language & Literature'),
		('Government', 'Government'),
		('History', 'History'),
		('History', 'History'),
		('Institute for International Peace Studies', 'Institute for International Peace Studies'),
		('Irish Language & Literature', 'Irish Language & Literature'),
		('Italian', 'Italian'),
		('Japanese', 'Japanese'),
		('Kinesiology', 'Kinesiology'),
		('Law', 'Law'),
		('Liberal Studies', 'Liberal Studies'),
		('Management & Administrative Sciences', 'Management & Administrative Sciences'),
		('Marketing', 'Marketing'),
		('Mathematics', 'Mathematics'),
		('Mathematics', 'Mathematics'),
		('MBA', 'MBA'),
		('MBA Program', 'MBA Program'),
		('Mechanical and Materials Engineering', 'Mechanical and Materials Engineering'),
		('Medical Biophysics', 'Medical Biophysics'),
		('Medicine', 'Medicine'),
		('Microbiology and Immunology', 'Microbiology and Immunology'),
		('Modern Languages and Literatures', 'Modern Languages and Literatures'),
		('Music', 'Music'),
		('Naval Science', 'Naval Science'),
		('Nursing', 'Nursing'),
		('Obstetrics and Gynaecology', 'Obstetrics and Gynaecology'),
		('Occupational Therapy', 'Occupational Therapy'),
		('Oncology', 'Oncology'),
		('Ophthalmology', 'Ophthalmology'),
		('Otolaryngology', 'Otolaryngology'),
		('Paediatrics', 'Paediatrics'),
		('Pathology', 'Pathology'),
		('Philosophy', 'Philosophy'),
		('Philosophy', 'Philosophy'),
		('Phsiology and Pharmacology', 'Phsiology and Pharmacology'),
		('Phys. Ed.', 'Phys. Ed.'),
		('Physical Education', 'Physical Education'),
		('Physical Medicine and Rehabilitation', 'Physical Medicine and Rehabilitation'),
		('Physical Therapy', 'Physical Therapy'),
		('Physics', 'Physics'),
		('Physics and Astronomy', 'Physics and Astronomy'),
		('Political Science', 'Political Science'),
		('Preprofessional Studies', 'Preprofessional Studies'),
		('Psychatry', 'Psychatry'),
		('Psychology', 'Psychology'),
		('Psychology', 'Psychology'),
		('Richard Ivey School of Business', 'Richard Ivey School of Business'),
		('Romance Language & Literature', 'Romance Language & Literature'),
		('Russian Languages & Literature', 'Russian Languages & Literature'),
		('Saint Mary\'s Art', 'Saint Mary\'s Art'),
		('Saint Mary\'s Education', 'Saint Mary\'s Education'),
		('Saint Mary\'s Mathematics', 'Saint Mary\'s Mathematics'),
		('Saint Mary\'s Religious Studies', 'Saint Mary\'s Religious Studies'),
		('Science (Non-Departmental)', 'Science (Non-Departmental)'),
		('Science, Technology, and Values', 'Science, Technology, and Values'),
		('Sociology', 'Sociology'),
		('Sociology', 'Sociology'),
		('Spanish', 'Spanish'),
		('Statistical and Actuarial Sciences', 'Statistical and Actuarial Sciences'),
		('Surgery', 'Surgery'),
		('Theology', 'Theology'),
		('Visual Arts', 'Visual Arts'),
	)
	department = models.CharField(max_length=255, choices=DEPARTMENTS)
	college = models.CharField(max_length=64, choices=COLLEGES)
	firstName = models.CharField(max_length=25)
	lastName = models.CharField(max_length=25)

	def __unicode__(self):
		return unicode('%s %s' % (self.firstName, self.lastName))
	def getColleges(self):
		return self.COLLEGES
	def getDepartments(self):
		return self.DEPARTMENTS

class Review(models.Model):
	professor = models.ForeignKey(Professor)
	poster = models.ForeignKey(User)
	course = models.CharField(max_length=64)
	year_taken = models.IntegerField()
	review = models.CharField(max_length=2048)
	
	def __unicode__(self):
		return unicode('%s review of %s %s' % (self.poster.username, self.professor.firstName, self.professor.lastName))

admin.site.register(Professor)
admin.site.register(Review)
