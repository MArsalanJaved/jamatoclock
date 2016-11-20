from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from restapi import views

urlpatterns = [
    url(r'^mosque/$', views.mosque_list),
    url(r'^mosque/(?P<pk>[\w\-]+)/$', views.mosques_detail),
    url(r'^timings/(?P<pk>[\w\-]+)/$', views.timings_detail),

]
urlpatterns = format_suffix_patterns(urlpatterns)
