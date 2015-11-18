from django import forms
from models import Professor, Review, Rating
from django.db.models.fields import BLANK_CHOICE_DASH

class ProfSearchForm(forms.Form):
	prof = Professor.objects.get(id=1)
	collegeSelect = forms.ChoiceField(label="College", choices=BLANK_CHOICE_DASH + list(prof.getColleges()), required=False)
	departmentSelect = forms.ChoiceField(label="Department", choices=BLANK_CHOICE_DASH + list(prof.getDepartments()), required=False)
	lastNameSearch = forms.CharField(label="Last Name", required=False)

class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = ['course', 'year_taken', 'review']

class RatingForm(forms.ModelForm):
	class Meta:
		model = Rating
		fields = ['overall', 'humor', 'difficulty', 'availability']
		labels = {
			'overall': 'Overall Rating: 1 is awful, 10 is incredible',
			'humor': 'Humor Rating: 1 is no humor, 10 is hilarious',
			'difficulty': 'Difficulty Rating: 1 is impossible, 10 is an easy A',
			'availability': 'Availability Rating: 1 is never, 10 is always'
		}

class ProfessorForm(forms.ModelForm):
	class Meta:
		model = Professor
		fields = ['department', 'college', 'firstName', 'lastName']
