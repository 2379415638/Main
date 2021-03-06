from django.conf.urls import url
from notes import views
urlpatterns = [
    url(r'time',views.time,name = 'time'),
    url(r'^$',views.index,name = 'index'),
    url(r'^topics/$',views.Topic,name = 'Topic'),
    url(r'^topics/(\d+)/$',views.topic,name='topic'),
    url(r'^topics/(\d+)/(\d+)/$',views.entry,name = 'entry'),
    url(r'^topics/user/$',views.user,name = 'user'),
    url(r'^pesonal/$',views.personal,name = 'person'),
    url(r'^create_topic/$',views.create_topic,name = 'create_topic'),
    url(r'^(\d+)del_topic/$',views.del_topic,name = 'del_topic'),
    url(r'^(\d+)/create_entry/$',views.create_entry,name = 'create_entry'),
    url(r'^(\d+)/(\d+)/edit_entry/$',views.edit_entry,name = 'edit_entry'),
    url(r'^(\d+)/(\d+)/del_entry/$',views.del_entry,name = 'del_entry'),
]