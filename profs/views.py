from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from models import Professor, Review
from forms import ProfSearchForm

@login_required
def profList(request):
	params = {
		'professors': Professor.objects.all()
	}
	return render(request, 'profList.html', params)

@login_required
def profView(request, profID):
	prof = Professor.objects.get(id=profID)
	params = {
		'professor': prof,
		'reviews': Review.objects.filter(professor=prof),
	}
	return render(request, 'profView.html', params)

@login_required
def profSearch(request):
	if request.method == 'POST':
		form = ProfSearchForm(request.POST)
		if form.is_valid():
			college = form.cleaned_data['collegeSelect']
			department = form.cleaned_data['departmentSelect']
			lastName = form.cleaned_data['lastNameSearch']
			params = {
				'professors': Professor.objects.filter(lastName__icontains=lastName).filter(college=college).filter(department=department),
			}
			return render(request, 'profList.html', params)
	else:
		form = ProfSearchForm()	
		params = {
			'form': form,
		}
		return render(request, 'profSearch.html', params)
