from django.conf.urls import url
from . import views

app_name = 'first_calendar'
urlpatterns = [
    #url(r'^index/$', views.index, name='index'),
    # the next line is a bad url pattern
    # url('', views.index,  name='index'),
    # use this:
    url('^$', views.index,  name='index'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
]