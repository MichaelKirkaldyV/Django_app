#gives us access to the url function
from django.conf.urls import url
#imports views.py in current folder
from . import views           # This line is new!

urlpatterns = [
	# "r" tells python to interpret what's after it as a raw string
  url(r'^$', views.index)   # This line has changed!
]
