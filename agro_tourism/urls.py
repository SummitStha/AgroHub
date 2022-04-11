from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.farm_list, name='farm_list'),
    url(r'^(?P<pk>[0-9]+)/farm-details$',
        views.farm_details, name='farm_detail'),
    url(r'^package-list$', views.package_list, name='package_list'),
    url(r'^farm-package-create$', views.FarmPackageCreateView.as_view(), name='farm_package_create'),
    url(r'^book-package$', views.BookPackageCreateView.as_view(), name='book_package'),

]
