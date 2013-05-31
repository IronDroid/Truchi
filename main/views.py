from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as social_logout

def index(request):
	print request.user.is_authenticated()
	if request.user.is_authenticated() == True:
		return redirect('home')
	return render_to_response('Truchi.html', {'titulo': 'Truchi'}, context_instance=RequestContext(request))
@login_required
def logout(request):
	social_logout(request)
	return redirect('index')

@login_required
def configuracion(request):
	print request.user.is_authenticated()
	return render_to_response('configuracion.html', {'titulo': 'Configuracion'}, context_instance=RequestContext(request))	

@login_required
def home(request):
	return render_to_response('home.html',{'titulo': 'home'}, context_instance=RequestContext(request))

@login_required
def perfil(request):
	return render_to_response('perfil.html',{'titulo': 'home'}, context_instance=RequestContext(request))

@login_required
def horario(request):
	return render_to_response('horario.html', {'titulo': 'GenHorario'}, context_instance=RequestContext(request))