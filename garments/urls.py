from django.conf.urls import url
from . import views

app_name = 'garments'

urlpatterns = [
    #/garments/
    url(r'^$', views.IndexView.as_view(), name = 'index'),
    #/garments/contact_us/
    url(r'^contact_us/$', views.Contact_us_View.as_view(), name='contact_us'),
    #/garments/about_us/
    url(r'^about_us/$', views.About_us_View.as_view(), name='about_us'),
    #/garments/gallery/men/
    url(r'^gallery/men/$', views.gallery_men, name='gallery men'),
    #/garments/gallery/women/
    url(r'^gallery/women/$', views.gallery_women, name='gallery women'),

    url(r'^(?P<product_id>[0-9]+)/view_details/$', views.detail, name='detail'),
]
