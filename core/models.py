from django.db import models

# Create your models here.
class Restaurante(models.Model):
	nome = models.CharField(max_length=100)
	TIPO = (
        ('CT','Contemporanea'),
        ('IT','Italiana'),
        ('JP','Japonesa'),
    )
	tipo = models.CharField(max_length=2, choices=TIPO)
	descricao = models.TextField()
	nota_media = models.FloatField()
	preco_medio = models.FloatField()
	horario_funcionamento = models.TimeField()
	site = models.CharField(max_length=100)
	data_cadastro = models.DateTimeField(auto_now_add=True)
	# foto = models.ImageField() # tem que instalar o PIL
	#horario_funcionamento = models.DateTimeField()
	#seg_abertura = models.TimeField()
	#seg_fechamento = models.TimeField()

	def __unicode__(self):
		return self.nome

class Evento(models.Model):
	nome = models.CharField(max_length=100)
	TIPO = (
        ('Shows','Shows'),
        ('Teatros','Teatros'),
    )
	tipo = models.CharField(max_length=15, choices=TIPO)
	descricao = models.TextField()
	nota_media = models.FloatField()
	preco_medio = models.FloatField()
	horario_funcionamento = models.TimeField()
	site = models.CharField(max_length=100)
	data_cadastro = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.nome

class Diversao(models.Model):
	nome = models.CharField(max_length=100)
	TIPO = (
        ('Museus', 'Museus'),
        ('+Conhecidos','+Conhecidos'),
        ('Boates','Boates'),
    )
	tipo = models.CharField(max_length=15, choices=TIPO)
	descricao = models.TextField()
	nota_media = models.FloatField()
	preco_medio = models.FloatField()
	horario_funcionamento = models.TimeField()
	site = models.CharField(max_length=100)
	data_cadastro = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.nome

class Comentario(models.Model):
	autor = models.CharField(max_length=100)
	conteudo = models.TextField()
	restaurante = models.ForeignKey('Restaurante')	