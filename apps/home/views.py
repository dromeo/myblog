from django.shortcuts import render_to_response
from django.template import RequestContext
from myblog.apps.ventas.models import cliente

def index_view(request):
		return render_to_response('home/index.html', context_instance=RequestContext(request))

def cliente_view(request):
	cli = cliente.objects.filter(status=True)
	ctx = {'cliente':cli}
	return render_to_response('home/cliente.html', ctx, context_instance=RequestContext(request))