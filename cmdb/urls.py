from django.conf.urls import include, url
from cmdb import views


urlpatterns = [  
        url(r'^$', views.index, name='index'),
	url(r'^index/', views.index, name='index'), 
	url(r'^register/', views.register, name='register'),
	url(r'^login/', views.login, name='login'),
]  
