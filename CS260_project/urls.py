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
urlpatterns += patterns('', (r'^signup$', home.signup), )
urlpatterns += patterns('', (r'^login$', home.login), )
urlpatterns += patterns('', (r'^logout$', home.logout), )
urlpatterns += patterns('', (r'^add-todo$', todo.add_todo), )
urlpatterns += patterns('', (r'^edit-todo/(?P<todo_id>\d+)$', todo.edit_todo), )
urlpatterns += patterns('', (r'^delete-todo/(?P<todo_id>\d+)$', todo.delete_todo), )
urlpatterns += patterns('', (r'^cancel-todo/(?P<todo_id>\d+)$', todo.cancel_todo), )
urlpatterns += patterns('', (r'^complete-todo/(?P<todo_id>\d+)$', todo.complete_todo), )

#urlpatterns += patterns('', (r'^$', home.main_page),
                            #(r'^user/(\w+)/$', home.user_page),
#                            (r'^login/$', 'django.contrib.auth.views.login'),
                            #(r'^logout/$', home.logout_page),
#                        )

#urlpatterns += patterns('', (r'^register/$', home.register_page), )