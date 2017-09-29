from django.conf.urls import url

from . import views

app_name = 'brlinkz'
urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^login/$', views.UserLogin.as_view(), name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^(?P<short_id>\w{6})$', views.redirect_original, name='redirectoriginal'),
    url(r'^makeshort/$', views.shorten_url, name='shortenurl'),
]