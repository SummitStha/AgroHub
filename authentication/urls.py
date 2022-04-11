from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from authentication import views

urlpatterns = [	
    url(r'^logout/$', auth_views.logout, name='logout'),
	url(r'^signup/$',views.UserSignupForm.as_view(), name='signup'),

]