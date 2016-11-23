from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from restapi import views

urlpatterns = [
    url(r'^mosque/$', views.mosque_list),
   	#url(r'^mosque/(?P<pk>[\w\-]+)/$', views.mosques_detail),
   	url(r'^timings/$', views.timings_list),
    url(r'^timings/(?P<pk>[\w\-]+)/$', views.timings_detail),
    url(r'^mosque/(?P<pk>[0-9]+)/$', views.mosques_detail), 

]
urlpatterns = format_suffix_patterns(urlpatterns)
