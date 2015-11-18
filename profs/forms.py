from django import forms
from models import Professor
from django.db.models.fields import BLANK_CHOICE_DASH

class ProfSearchForm(forms.Form):
	prof = Professor.objects.get(id=1)
	collegeSelect = forms.ChoiceField(label="College", choices=BLANK_CHOICE_DASH + list(prof.getColleges()), required=False)
	departmentSelect = forms.ChoiceField(label="Department", choices=BLANK_CHOICE_DASH + list(prof.getDepartments()), required=False)
	lastNameSearch = forms.CharField(label="Last Name")
