from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from forms import ProfSearchForm, ReviewForm, RatingForm, ProfessorForm
from models import Professor, Review, Rating
from django.shortcuts import render

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
			profs = Professor.objects.all()
			if college != '':
				profs = profs.filter(college=college)	
			if department != '':
				profs = profs.filter(department=department)
			if lastName != '':
				profs = profs.filter(lastName__icontains=lastName)
			params = {
				'professors': profs
			}
			return render(request, 'profList.html', params)
		else:
			return render(request, 'profList.html', {'professors': Professor.objects.all()})	
	else:
		form = ProfSearchForm()	
		params = {
			'form': form,
		}
		return render(request, 'profSearch.html', params)

@login_required
def add_review(request, profID):
	if request.method == 'POST':
		form = ReviewForm(request.POST)
		if form.is_valid():
			review = Review()
			review.professor = Professor.objects.get(id=profID)
			review.poster = request.user
			review.course = form.cleaned_data['course']	
			review.year_taken = form.cleaned_data['year_taken']	
			review.review = form.cleaned_data['review']	
			review.save()
		return HttpResponseRedirect('/accounts/profs/profID/' + str(review.professor.id) + '/')
	else:
		form = ReviewForm()
		params = {
			'form': form,
		}
		return render(request, 'profSearch.html', params)

@login_required
def add_rating(request, profID):
	if request.method == 'POST':
		form = RatingForm(request.POST)
		if form.is_valid():
			rating = Rating()
			rating.professor = Professor.objects.get(id=profID)
			rating.overall = form.cleaned_data['overall']
			rating.humor = form.cleaned_data['humor']
			rating.difficulty = form.cleaned_data['difficulty']
			rating.availability = form.cleaned_data['availability']
			rating.save()
		return HttpResponseRedirect('/accounts/profs/profID/' + profID + '/')
	else:
		form = RatingForm()
		params = {
			'form': form,
		}
		return render(request, 'profSearch.html', params)

@login_required
def add_prof(request):
	if request.method == 'POST':
		form = ProfessorForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('accounts/profs/profSearch/')
	else:
		form = ProfessorForm()
		params = {
			'form': form,
		}
		return render(request, 'profSearch.html', params)
