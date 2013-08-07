from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as social_logout
from main.models import Estudiante, Materia

def index(request):
	if request.user.is_authenticated() == True:
		return redirect('home')
	return render_to_response('Truchi.html', {'titulo': 'Truchi'}, context_instance=RequestContext(request))

@login_required
def logout(request):
	social_logout(request)
	return redirect('index')

@login_required
def configuracion(request):
	est = Estudiante.objects.get(username=request.user.username)
	return render_to_response('configuracion.html', {
			'titulo': 'Configuracion', 
			'subtitle': 'Config',
			'nombre': est.nombre,
			'email': est.email,
			'avatar': est.avatar
		}, context_instance=RequestContext(request))	

@login_required
def home(request):
	est = Estudiante.objects.get(username=request.user.username)
	user_data = {'titulo': 'home','nombre': est.nombre, 'avatar': est.avatar}
	return render_to_response('home.html', user_data, context_instance=RequestContext(request))

@login_required
def perfil(request):
	est = Estudiante.objects.get(username=request.user.username)
	user_data = {'titulo': 'perfil','nombre': est.nombre, 'avatar': est.avatar}
	return render_to_response('perfil.html', user_data, context_instance=RequestContext(request))

@login_required
def horario(request):
	est = Estudiante.objects.get(username=request.user.username)
	user_data = {'titulo': 'horario','nombre': est.nombre, 'avatar': est.avatar}
	return render_to_response('horario.html', user_data, context_instance=RequestContext(request))

@login_required
def generador(request):
	est = Estudiante.objects.get(username=request.user.username)
	matSigla = list()
	if est.is_url_horarios:
		materias = Materia.objects.filter(estudiante=est)
		for materia in materias:
			matSigla.append(materia.sigla)
	user_data = {'titulo': 'Generador','nombre': est.nombre, 'avatar': est.avatar, 'horarios': est.is_url_horarios, 'siglas_materia':matSigla}
	return render_to_response('generador.html', user_data, context_instance=RequestContext(request))