from django.conf.urls import url
from django.contrib import admin

from colleges import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'colleges/$', views.schools_list, name='schools_list'),
    url(r'^admin/', admin.site.urls),
]
