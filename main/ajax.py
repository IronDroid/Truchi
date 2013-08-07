from main.models import *
from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from bs4 import BeautifulSoup
import urllib2

@dajaxice_register
def combinacion(request, lista):
	materias = lista.split(';')
	simbolos = list()
	for materia in materias:
		m = Materia.objects.get(sigla = materia)
		for paralelo in Paralelo.objects.filter(id_materia = m):
			simbolos.append(materia+paralelo.sigla_paralelo)
	
	combinaciones = combinacionMaterias(simbolos, materias)

	listgen = []
	diasT = ('LUNES','MARTES','MIERCOLES','JUEVES','VIERNES','SABADO')
	horasT = ('08:00','10:00','12:00','14:00','16:00','18:00','20:00')
	sw = True
	for combinacion in combinaciones:
		genhorario = [ [""] * 7 for x in [''] * 6]
		for mat in combinacion:
			sw = True
			nombre_mat = mat[:7]
			materia = Materia.objects.get(sigla = nombre_mat)
			sigla_par = mat[7:]
			paralelo = Paralelo.objects.get(id_materia = materia, sigla_paralelo = sigla_par)
			horario = Horario.objects.filter(id_paralelo = paralelo)
			for hora in horario:
				if genhorario[diasT.index(hora.dia)][horasT.index(hora.hora_inicio)] == '':
					genhorario[diasT.index(hora.dia)][horasT.index(hora.hora_inicio)] = nombre_mat
				else:
					sw = False
					print 'CHOQUE'
					break
		if sw:
			listgen.append(genhorario)
	# return simplejson.dumps({'combinaciones':len(combinaciones), 'horarios':len(listgen)})
	return simplejson.dumps({'listgen':listgen})


@dajaxice_register
def materias_inscritas(request, urltext):
	print request
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
def guardar_materias(request, urltextt):
	url = urltextt
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page.read())
	tables= soup('table') #the main table
	num = 0
	matlist = []
	est = Estudiante.objects.get(username=request.user.username)
	print est.nombre
	for td in tables[1](['td','th']):
		num += 1
		if td.get('nowrap') == None:
			tdtext='-|-'.join(td(text=True)).strip()
			if num == 2:
				est.cod_estudiante = tdtext
	try:
		print est.cod_estudiante
		if Estudiante.objects.get(cod_estudiante=est.cod_estudiante):
			print 'existe!!! salir'
			est = Estudiante.objects.get(cod_estudiante=est.cod_estudiante)
			mats = Materia.objects.filter(estudiante=est)
			for matx in mats:
				matlist.append(matx.sigla)
			return simplejson.dumps({'materias': matlist})
	except Exception, e:
		print 'no existe, guardar y continuar'
		est.is_url_horarios = True
		est.save()
	count = 0
	subcount1 = 0
	linea = ''
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
				mat.save()
				print 'guardar materia'
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
				print 'save paralelos'
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
					print 'save horarios'
				count = 0
				linea = ''
	mats = Materia.objects.filter(estudiante=est)
	for matx in mats:
		matlist.append(matx.sigla)
	print 'retorna Json'
	return simplejson.dumps({'materias': matlist})

def combinations(iterable, r):
    pool = iterable
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

def combinacionMaterias(simbolos, materias):
	S = materias
	# S = ['a','b','c','d']
	num_materias = len(S)
	l = simbolos
	res = list()
	for x in combinations(l, num_materias):
		sw = True;
		cad = ' '.join(list(x))
		for mats in S:
			if cad.count(mats) != 1:
				sw = False
				break
		if sw:
			res.append(x)
	return res