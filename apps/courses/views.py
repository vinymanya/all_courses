# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from .models import Course
from django.contrib.messages import error

# Create your views here.
def index(request):
	context = {
		"courses": Course.objects.all()
	}
	#same as "SELECT * FROM courses"
	return render(request, "courses/index.html", context)


def create(request):
	if request.method == "POST":
		errors = Course.objects.validate(request.POST)
		if len(errors):
			for field, message in errors.iteritems():
				error(request, message, extra_tags = field)
				return redirect("/")
		else:
			#create a new course
			Course.objects.create(
				name = request.POST["name"],
				desc = request.POST["desc"]
				)
			#This is same as "INSERT INTO courses(name, desc, created_at, updated_at) VALUES(:name, :desc, NOW(), NOW())"
			return redirect("/")

def confirm(request, id):
	context = {
		"course": Course.objects.get(id=id)
	}
	return render(request, "courses/confirm.html", context)

def delete(request, id):
	Course.objects.get(id=id).delete()
	return redirect("/")
