
from django.conf.urls import url, include
from django.contrib import admin

from views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^TodoList/', todolist, name='TodoList'),
    url(r'^addtodo/$', addtodo, name='add'),
    url(r'^todofinish/(?P<id>\d+)/$', todofinish, name='finish'),
    url(r'^todobackout/(?P<id>\d+)/$', todoback,  name='backout'),
    url(r'^updatetodo/(?P<id>\d+)/$', updatetodo, name='update'),
    url(r'^tododelete/(?P<id>\d+)/$', tododelete, name='delete'),
]
