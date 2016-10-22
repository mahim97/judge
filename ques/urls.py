from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.index,name='index'),
    url(r'^(?P<prob_code>[a-zA-Z0-9]+)/detail/$', views.detail, name='detail'),
    
]
