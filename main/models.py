from django.db import models

class Estudiante(models.Model):
	cod_estudiante = models.CharField(max_length=12, primary_key=True)
	nombre = models.CharField(max_length=30)
	periodo = models.CharField(max_length=5)
	username = models.TextField(unique=True)
	avatar = models.TextField()

	def __unicode__(self):
		return self.nombre

class Materia(models.Model):
	sigla = models.CharField(max_length=10, primary_key=True)
	nombre = models.CharField(max_length=15)
	estudiante = models.ForeignKey('Estudiante')

	def __unicode__(self):
		return self.nombre

class Paralelo(models.Model):
	nombre_docente = models.TextField()
	sigla_paralelo = models.TextField()
	id_materia = models.ForeignKey('Materia')

	def __unicode__(self):
		return self.nombre_docente

class Horario(models.Model):
	dia = models.TextField()
	hora_inicio = models.TextField()
	hora_final = models.TextField()
	aula = models.TextField()
	id_paralelo = models.ForeignKey('Paralelo')

	def __unicode__(self):
		return self.aula
