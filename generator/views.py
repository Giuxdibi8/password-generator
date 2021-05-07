from django.shortcuts import render
from django.http import HttpResponse
import random 

# Create your views here.

def home(request):
	return render (request,'generator/home.html')

def about(request):
	return render (request,'generator/about.html')

def password(request):
	
	charachters = list('abcdefghilmnopqrstuzyxkjz')

	if request.GET.get('uppercase'):
		charachters.extend(list('ABCDEFGHILMNOPQRSTUVZYJKX'))
	if request.GET.get('special charachters'):
		charachters.extend(list('@!"£$%&/()=?^|'))
	if request.GET.get('numbers'):
		charachters.extend(list('0123456789'))

	lenght=int(request.GET.get('lenght'))

	thepassword=''
	for i in range (lenght):
		thepassword += random.choice(charachters)

	return render (request,'generator/password.html',{'password':thepassword})