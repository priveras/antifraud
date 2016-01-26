from django.conf.urls import include, url

from . import views

app_name = 'data'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]