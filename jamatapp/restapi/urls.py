from django.conf.urls import url , include
from rest_framework.urlpatterns import format_suffix_patterns
from restapi import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'mosques', views.mosque_list , 'mosques')
router.register(r'time', views.time_list , 'time')
#router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

'''urlpatterns = [
    url(r'^mosque/$', views.mosque_list , name = 'mosque-list'),
   	#url(r'^mosque/(?P<gmap_id>.+)/$', views.mosques_detail.as_view()),
   	#url(r'^timings/$', views.timings_list),
    #url(r'^timings/(?P<pk>[\w\-]+)/$', views.timings_detail),
    url(r'^mosque/(?P<pk>[\w\-]+)/$', views.mosques_detail), 

]
urlpatterns = format_suffix_patterns(urlpatterns)'''
