from django.conf.urls import url
from django.contrib import admin

from colleges import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'colleges/$', views.schools_list, name='schools_list'),
    url(r'resources/$', views.resources, name='resources'),
    url(r'faq/$', views.faq, name='faq'),
    url(r'checklist/$', views.checklist, name='checklist'),
    url(r'ambassadors/$', views.ambassadors, name='ambassadors'),
    url(r'^admin/', admin.site.urls),
]
