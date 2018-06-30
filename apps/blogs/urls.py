#gives us access to the url function
from django.conf.urls import url
#imports views.py in current folder
from . import views           # This line is new!

urlpatterns = [
	# "r" tells python to interpret what's after it as a raw string
  url(r'^blogs$', views.index),
  url(r'^new$',views.new),
  url(r'^create$',views.create),
  url(r'^(?P<number>\d+)$',views.show),
  url(r'^(?P<number>\d+)/edit$',views.edit),
  url(r'^(?P<number>\d+)/delete$',views.delete)
]
