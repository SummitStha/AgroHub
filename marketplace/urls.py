from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ProductListView.as_view(),  name='product_list'),
    url(r'^product-create$', views.ProductCreateView.as_view(),  name='product_create'),
    url(r'^buyer-form-create$', views.BuyerFormCreateView.as_view(),
        name='buyer_form_create'),
    url(r'^request-product$', views.RequestProductView.as_view(),
        name='request_create'),
    url(r'^buyer-list$', views.BuyerListView.as_view(),
        name='buyer_list'),
    url(r'^selling-list$', views.BuyerListView.as_view(),
        name='selling_list'),

]
