from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect
from django.contrib.auth import logout
from django.template import RequestContext
import datetime
from django.core.mail import send_mail, BadHeaderError

def index(request):
	return render_to_response('index.html',{'title':'Index'})

def about(request):
	return render_to_response('about_us.html',{'title':'Sobre nosotros'})

def home(request):
	return render_to_response('home.html',{'title':'Home'})


def help(request):
	return render_to_response('help.html', {'title':'Ayuda'})

def contact(request):
	return render_to_response('contact.html', {'title':'Contacto'})
