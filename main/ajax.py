from main.models import *
from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from bs4 import BeautifulSoup
import urllib2

@dajaxice_register
def materias_inscritas(request, urltext):
	url = urltext
	if urltext == "":
		return None
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page.read())
	tables= soup('table') #the main table
	num = 0
	cell = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado"] 
	row = []
	row.append(cell)
	cell = []
	for td in tables[4](['td','th']):
		if td.get('style') != None:
			tdtext=' '.join(td(text=True)).strip()
			num = num + 1
			if tdtext == "":
				cell.append("&nbsp;")
			else:
				cell.append(tdtext[0:7])
			if num % 6 == 0:
				row.append(cell)
				cell = []
	return simplejson.dumps({'row': row})

# guarda a base de datos
@dajaxice_register
def materias(request, urltextt):
	url = urltextt
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page.read())
	tables= soup('table') #the main table
	num = 0;
	est = Estudiante()
	for td in tables[1](['td','th']):
		num += 1
		if td.get('nowrap') == None:
			tdtext='-|-'.join(td(text=True)).strip()
			if num == 2:
				# print cod_est
				est.cod_estudiante = tdtext
			if num == 4:
				# print nombre_est
				est.nombre = tdtext
	for td in tables[2](['td','th']):
		if td.get('nowrap') == None:
			tdtext='-|-'.join(td(text=True)).strip()
			if len(tdtext) < 5:
				# print periodo
				est.periodo = tdtext
	try:
		if Estudiante.objects.get(cod_estudiante=est.cod_estudiante):
			print 'existe!!! salir'
			return
	except Exception, e:
		print 'no existe, guardar y continuar'
		est.save()
	count = 0
	subcount1 = 0;
	linea = '';
	for td in tables[3](['td','th']):
		# nombre de las materias todas
		if td.get('colspan') != None:
			tdtext='|'.join(td(text=True)).strip()
			if tdtext[:1] == '[':
				mat = Materia()
				tdtext = tdtext[4:].strip()
				sigla_materia = tdtext[:7].strip()
				# sigla_materia
				mat.sigla = sigla_materia
				# nombre_materia
				nombre_materia = tdtext[7:].strip()
				mat.nombre = nombre_materia
				mat.estudiante = est
				print 'guardar materia'
				mat.save()
		# paralelos
		elif td.get('style') != None or td.get('colspan') != None:
			tdtext='$'.join(td(text=True)).strip()
			count += 1
			linea = linea +'|'+ tdtext
			if count == 3:
				partes = linea[1:].split('|')
				par = Paralelo()
				# nombre_docente
				nombre_docente = partes[0]
				par.nombre_docente = nombre_docente
				# sigla_paralelo
				sigla_paralelo = partes[1]
				par.sigla_paralelo = sigla_paralelo
				par.id_materia = mat
				par.save()
				horario = partes[2]
				horas = horario.split('$')
				for hora in horas:
					hor = Horario()
					# dia
					hor.dia = hora[:hora.find(' ')].strip()
					hour = hora[hora.find(' '):hora.find('(')].strip()
					hours = hour.split(' - ')
					# hora_inicio
					hor.hora_inicio = hours[0]
					# hora_final
					hor.hora_final = hours[1]
					# aula
					hor.aula = hora[hora.find('('):].strip()
					# id_paralelo
					hor.id_paralelo = par
					hor.save()
				count = 0
				linea = ''
