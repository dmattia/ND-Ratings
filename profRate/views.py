from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from forms import UserCreateForm
from django.contrib import auth

def login(request):
	c = {
		'next': request.GET['next'],
	}
	c.update(csrf(request))
	return render_to_response('login.html', c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect(request.POST['next'])
		#return HttpResponseRedirect('/accounts/loggedin/')
	else:
		return HttpResponseRedirect('/accounts/invalid/')

def loggedin(request):
	return HttpResponseRedirect(request.POST['next'])
	#return HttpResponseRedirect('/accounts/profs/profSearch')

def invalid_login(request):
	return render_to_response('invalid_login.html')

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')

def register_user(request):
	if request.method == 'POST':
		form = UserCreateForm(request.POST)
		if form.is_valid():
			# check if email is already being used
			if User.objects.filter(email__iexact=form.cleaned_data['email']).count > 0:
				args = {
					'message': 'This email is already in use',
				}
				return render_to_response('message.html', args)
			form.save()
			return HttpResponseRedirect('/accounts/register_success/')
		else:
			args = {}
			args.update(csrf(request))
			args['registerForm'] = form
			return render_to_response('register.html',args)
	else:
		# first time on register page
		args = {}
		args.update(csrf(request))
		args['registerForm'] = UserCreateForm()
		return render_to_response('register.html',args)

def register_success(request):
	return render_to_response('register_success.html')

def register_failure(request):
	return render_to_response('register_failure.html')
