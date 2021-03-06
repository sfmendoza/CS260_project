from django.conf.urls import patterns, include, url
from lists.views import home
from lists.views import todo
from django.contrib import admin
import os.path

admin.autodiscover()

site_media = os.path.join(os.path.dirname(__file__), 'site_media')

admin.autodiscover()

urlpatterns = patterns('', url(r'^admin/', include(admin.site.urls)), )
urlpatterns += patterns('', (r'^$', home.main_page), )
urlpatterns += patterns('', (r'^register/signup$', home.signup), )
urlpatterns += patterns('', (r'^login/$', home.login), )
urlpatterns += patterns('', (r'^login/login_user$', home.login_user), )
urlpatterns += patterns('', (r'^user_page/update', home.update), )
urlpatterns += patterns('', (r'^register/$', home.register), )
urlpatterns += patterns('', (r'^logout$', home.logout), )
urlpatterns += patterns('', (r'^add-todo$', todo.add_todo), )
urlpatterns += patterns('', (r'^edit-todo/(?P<todo_id>\d+)$', todo.edit_todo), )
urlpatterns += patterns('', (r'^delete-todo/(?P<todo_id>\d+)$', todo.delete_todo), )
urlpatterns += patterns('', (r'^cancel-todo/(?P<todo_id>\d+)$', todo.cancel_todo), )
urlpatterns += patterns('', (r'^complete-todo/(?P<todo_id>\d+)$', todo.complete_todo), )