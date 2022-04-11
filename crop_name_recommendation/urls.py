from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from authentication import views as _views
urlpatterns = [
    url(r'^login_option/$', views.loginoption, name='login_option'),
    url(r'^research/$', views.researchhub, name='research_hub'),
    url(r'^details/$', views.index, name='research_details'),
    url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'crop_name_recommendation/login.html'}, name='login'),
    url(r'^signup/$', _views.UserSignupForm.as_view(), name='signup'),
    url(r'^svm/$', views.svm, name='svm'),
    url(r'^naivebayes/$', views.naivebayes, name='naivebayes'),
    url(r'^neuralnetwork/$', views.neuralnetwork, name='neuralnetwork'),
    url(r'^randomforest/$', views.randomforest, name='randomforest'),
    url(r'^naive_bayes_algo/$', views.naiveBayesAlgo, name='naive_bayes_algo'),
    url(r'^svm_algo/$', views.svmAlgo, name='svm_algo'),
    url(r'^neural_network_algo/$', views.neuralNetworkAlgo, name='neural_network_algo'),
    url(r'^random_forest_algo/$', views.randomForestAlgo, name='random_forest_algo'),
    url(r'^e_algo/$', views.runEAlgo, name='e_algo'),
    url(r'^ensembleTech/$', views.ensembleTech, name='ensembleTech'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^aboutus/$', views.aboutus, name='aboutus'),
    url(r'^contactus/$', views.contactus, name='contactus'),
    url(r'^fileupload/$', views.fileupload, name='fileupload'),
    url(r'^data-collection/$', views.SoilDataCollectionFormView.as_view(),  name='data_collection'),
    url(r'^research_hub/export-to-csv/$', views.exportCsv, name='export-csv'),
    url(r'^research_hub/export-to-json/$', views.exportJson, name='export-json'),
    url(r'^research_hub/export-to-excel/$', views.exportExcel, name='export-excel'),
]
