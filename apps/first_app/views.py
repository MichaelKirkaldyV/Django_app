# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect #imports http response to server and redirect

# Create your views here.
#Index function is called when the root is visited.
def index(request):
	response = "Hello, I am your first request!"
	return HttpResponse(response)
