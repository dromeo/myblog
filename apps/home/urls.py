from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('myblog.apps.home.views',
						url(r'^$','index_view',name='vista_principal'),
						url(r'^cliente/$','cliente_view', name='vista_cliente'),
)