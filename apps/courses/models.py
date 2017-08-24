# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseManager(models.Manager):
	def validate(self, post_data):
		errors = {}
		print errors
		# print post_data
		for field, value in post_data.iteritems():
			if len(value) < 1:
				errors[field] = "{} field is required!".format(field.replace('_', ''))

			if field == "name":
				if not field in errors and len(value) < 5:
					errors[field] = "{} field must be at least 5 characters".format(field.replace('_',''))
			if field == "desc":
				if not field in errors and len(value) < 15:
					errors[field] = "{} field must be at least 15 characters".format(field.replace('_',''))
		return errors

class Course(models.Model):
	name = models.CharField(max_length = 100)
	desc = models.TextField(max_length = 1000)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = CourseManager()

	def __str(self):
		print "name: {}, desc: {}".format(self.name, self.desc)
