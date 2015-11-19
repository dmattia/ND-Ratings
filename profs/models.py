from django.contrib.auth.models import User
from django.db.models import Avg
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
		('Accountancy', 'Accountancy'),
		('Aerospace and Mechanical Engr.', 'Aerospace and Mechanical Engr.'),
		('Africana Studies', 'Africana Studies'),
		('Air Force-Aerospace Studies', 'Air Force-Aerospace Studies'),
		('American Studies', 'American Studies'),
		('Anthropology', 'Anthropology'),
		('Applied & Comp Math and Stats', 'Applied & Comp Math and Stats'),
		('Arabic Language and Literature', 'Arabic Language and Literature'),
		('Architecture', 'Architecture'),
		('Art History', 'Art History'),
		('Art Studio', 'Art Studio'),
		('Art,Art History,& Design (SMC)', 'Art,Art History,& Design (SMC)'),
		('Arts and Letters (Non-dept.)', 'Arts and Letters (Non-dept.)'),
		('Arts and Letters - Honors', 'Arts and Letters - Honors'),
		('Asian Studies', 'Asian Studies'),
		('Biological Sciences', 'Biological Sciences'),
		('Biology (SMC)', 'Biology (SMC)'),
		('Bus Admin - Business Law', 'Bus Admin - Business Law'),
		('Bus Admin - Communication', 'Bus Admin - Communication'),
		('Bus Admin - Entrepreneurship', 'Bus Admin - Entrepreneurship'),
		('Bus Admin - Ethics', 'Bus Admin - Ethics'),
		('Bus Admin - Management', 'Bus Admin - Management'),
		('Business Administration', 'Business Administration'),
		('Business Administration (SMC)', 'Business Administration (SMC)'),
		('Business Administration - A&L', 'Business Administration - A&L'),
		('Business Administration - EG', 'Business Administration - EG'),
		('Business Administration - SC', 'Business Administration - SC'),
		('Business Administration - UG', 'Business Administration - UG'),
		('Catholic Social Tradition', 'Catholic Social Tradition'),
		('Center for Social Concerns', 'Center for Social Concerns'),
		('Chemical & Biomolecular Engr.', 'Chemical & Biomolecular Engr.'),
		('Chemistry and Biochemistry', 'Chemistry and Biochemistry'),
		('Chinese', 'Chinese'),
		('Civil Engineering', 'Civil Engineering'),
		('Classics in Translation', 'Classics in Translation'),
		('College Seminar', 'College Seminar'),
		('Communications (SMC)', 'Communications (SMC)'),
		('Communicative Sciences (SMC)', 'Communicative Sciences (SMC)'),
		('Computer Science (SMC)', 'Computer Science (SMC)'),
		('Computer Science and Engr.', 'Computer Science and Engr.'),
		('Computing & Digtl Technologies', 'Computing & Digtl Technologies'),
		('Constitutional Studies', 'Constitutional Studies'),
		('Ctr for Study of Lang&Cultures', 'Ctr for Study of Lang&Cultures'),
		('Dance (SMC)', 'Dance (SMC)'),
		('Design', 'Design'),
		('Doctor of Musical Arts', 'Doctor of Musical Arts'),
		('EG, SC & Tech Entrepreneurship', 'EG, SC & Tech Entrepreneurship'),
		('East Asian Lang & Lit', 'East Asian Lang & Lit'),
		('Economics', 'Economics'),
		('Education', 'Education'),
		('Education (SMC)', 'Education (SMC)'),
		('Education, School and Society', 'Education, School and Society'),
		('Electrical Engineering', 'Electrical Engineering'),
		('Energy Studies', 'Energy Studies'),
		('Eng., Science, Tech. & Society', 'Eng., Science, Tech. & Society'),
		('Engineering (Non-Departmental)', 'Engineering (Non-Departmental)'),
		('English', 'English'),
		('English Language School (SMC)', 'English Language School (SMC)'),
		('English Literature (SMC)', 'English Literature (SMC)'),
		('English Writing (SMC)', 'English Writing (SMC)'),
		('Environmental Geosciences', 'Environmental Geosciences'),
		('Environmental Studies (SMC)', 'Environmental Studies (SMC)'),
		('Film, Television, and Theatre', 'Film, Television, and Theatre'),
		('Finance', 'Finance'),
		('First Year of Studies', 'First Year of Studies'),
		('French', 'French'),
		('French - Translation (SMC)', 'French - Translation (SMC)'),
		('Gender & Women\'s Studies (SMC)', 'Gender & Women\'s Studies (SMC)'),
		('Gender Studies', 'Gender Studies'),
		('German', 'German'),
		('Gerontology (SMC)', 'Gerontology (SMC)'),
		('Global Health - Eck Institute', 'Global Health - Eck Institute'),
		('Global Studies (SMC)', 'Global Studies (SMC)'),
		('Graduate Education', 'Graduate Education'),
		('Greek Language and Literature', 'Greek Language and Literature'),
		('Hebrew Language and Literature', 'Hebrew Language and Literature'),
		('Hesburgh Prg in Public Service', 'Hesburgh Prg in Public Service'),
		('History', 'History'),
		('History and Phil. of Science', 'History and Phil. of Science'),
		('Humanistic Studies (SMC)', 'Humanistic Studies (SMC)'),
		('Indiana U. Sch of Med. S. Bend', 'Indiana U. Sch of Med. S. Bend'),
		('Inst. for Int\'l Peace Studies', 'Inst. for Int\'l Peace Studies'),
		('Integrated Biomedical Sciences', 'Integrated Biomedical Sciences'),
		('Intercultural Studies (SMC)', 'Intercultural Studies (SMC)'),
		('Internatnl Development Studies', 'Internatnl Development Studies'),
		('Irish Language and Literature', 'Irish Language and Literature'),
		('Irish Studies', 'Irish Studies'),
		('Italian', 'Italian'),
		('Japanese', 'Japanese'),
		('Journalism, Ethics & Democracy', 'Journalism, Ethics & Democracy'),
		('Justice Studies (SMC)', 'Justice Studies (SMC)'),
		('Korean', 'Korean'),
		('Latin American Studies', 'Latin American Studies'),
		('Latin Language and Literature', 'Latin Language and Literature'),
		('Latino Studies', 'Latino Studies'),
		('Law', 'Law'),
		('Literature', 'Literature'),
		('MBA Bus Communications', 'MBA Bus Communications'),
		('MBA Business Ethics', 'MBA Business Ethics'),
		('MBA Chicago', 'MBA Chicago'),
		('MBA Executive Program', 'MBA Executive Program'),
		('MBA General', 'MBA General'),
		('Management', 'Management'),
		('Management - Consulting', 'Management - Consulting'),
		('Management - Entrepreneurship', 'Management - Entrepreneurship'),
		('Management - IT', 'Management - IT'),
		('Marketing', 'Marketing'),
		('Master of Nonprofit Admin.', 'Master of Nonprofit Admin.'),
		('Master of Sacred Music', 'Master of Sacred Music'),
		('Master of Sc in Bus Analytics', 'Master of Sc in Bus Analytics'),
		('Master of Science in Finance', 'Master of Science in Finance'),
		('Master of Science in Mgtment', 'Master of Science in Mgtment'),
		('Mathematics', 'Mathematics'),
		('Medieval Institute', 'Medieval Institute'),
		('Middle Eastern Studies', 'Middle Eastern Studies'),
		('Military Science (Army ROTC)', 'Military Science (Army ROTC)'),
		('Modern and Classical Languages', 'Modern and Classical Languages'),
		('Music', 'Music'),
		('Naval Science (ROTC)', 'Naval Science (ROTC)'),
		('Nursing (SMC)', 'Nursing (SMC)'),
		('Patent Law', 'Patent Law'),
		('Patent Law Masters', 'Patent Law Masters'),
		('Philosophy', 'Philosophy'),
		('Philosophy, Religion and Lit', 'Philosophy, Religion and Lit'),
		('Physical Education', 'Physical Education'),
		('Physics', 'Physics'),
		('Political Science', 'Political Science'),
		('Political Science (SMC)', 'Political Science (SMC)'),
		('Portuguese', 'Portuguese'),
		('Poverty Studies', 'Poverty Studies'),
		('Program of Liberal Studies', 'Program of Liberal Studies'),
		('Psychology', 'Psychology'),
		('Psychology (SMC)', 'Psychology (SMC)'),
		('Registrar\'s Office', 'Registrar\'s Office'),
		('Religious Studies (SMC)', 'Religious Studies (SMC)'),
		('Romance Lang & Lit', 'Romance Lang & Lit'),
		('Russian', 'Russian'),
		('Science (Non-departmental)', 'Science (Non-departmental)'),
		('Science Preprofessional', 'Science Preprofessional'),
		('Science, Technology and Values', 'Science, Technology and Values'),
		('Self Designed Major (SMC)', 'Self Designed Major (SMC)'),
		('Social Work (SMC)', 'Social Work (SMC)'),
		('Sociology', 'Sociology'),
		('Spanish', 'Spanish'),
		('St. Mary\'s', 'St. Mary\'s'),
		('Sustainability', 'Sustainability'),
		('Syriac Language and Literature', 'Syriac Language and Literature'),
		('Theatre (SMC)', 'Theatre (SMC)'),
		('Theology', 'Theology'),
		('Writing and Rhetoric', 'Writing and Rhetoric'),
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
	def overall(self):
		return Rating.objects.filter(professor=self).aggregate(average_overall=Avg('overall'))['average_overall']
	def availability(self):
		return Rating.objects.filter(professor=self).aggregate(average_availability=Avg('availability'))['average_availability']
	def difficulty(self):
		return Rating.objects.filter(professor=self).aggregate(average_difficulty=Avg('difficulty'))['average_difficulty']
	def humor(self):
		return Rating.objects.filter(professor=self).aggregate(average_humor=Avg('humor'))['average_humor']

class Review(models.Model):
	professor = models.ForeignKey(Professor)
	poster = models.ForeignKey(User)
	course = models.CharField(max_length=64)
	year_taken = models.IntegerField()
	review = models.TextField(max_length=2048)
	
	def __unicode__(self):
		return unicode('%s review of %s %s' % (self.poster.username, self.professor.firstName, self.professor.lastName))

class Rating(models.Model):
	RATINGS = (
		('1', '1'),
		('2', '2'),
		('3', '3'),
		('4', '4'),
		('5', '5'),
		('6', '6'),
		('7', '7'),
		('8', '8'),
		('9', '9'),
		('10', '10'),
	)
	professor = models.ForeignKey(Professor, null=True)
	poster = models.ForeignKey(User, null=True)
	humor = models.CharField(max_length=2, choices=RATINGS, null=True)
	difficulty = models.CharField(max_length=2, choices=RATINGS, null=True)
	availability = models.CharField(max_length=2, choices=RATINGS, null=True)
	overall = models.CharField(max_length=2, choices=RATINGS, null=True)
	
	def __unicode__(self):
		return unicode('%s rate of %s %s' % (self.poster.username, self.professor.firstName, self.professor.lastName))

admin.site.register(Professor)
admin.site.register(Review)
admin.site.register(Rating)
