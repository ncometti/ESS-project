from django.db import models

# Create your models here.
class Restaurante(models.Model):
	nome = models.CharField(max_length=100)
	TIPO = (
        ('Contemporanea','Contemporanea'),
        ('Italiano','Italiano'),
        ('Japones','Japones'),
        ('Fast food', 'Fast food'),
        ('Pizzaria', 'Pizzaria'),
        ('Chines', 'Chines'),
        ('Sorveteria', 'Sorveteria'),
        ('Doceria', 'Doceria'),
        ('Creperia', 'Creperia')
    )
	tipo = models.CharField(max_length=20, choices=TIPO)
	descricao = models.TextField()
	nota_media = models.FloatField()
	preco_medio = models.FloatField()
	site = models.CharField(max_length=100)
	data_cadastro = models.DateTimeField(auto_now_add=True)
	
	# foto = models.ImageField() # tem que instalar o PIL
	#horario_funcionamento = models.DateTimeField()
	dom_abertura = models.TimeField()
	dom_fechamento = models.TimeField()
	seg_abertura = models.TimeField()
	seg_fechamento = models.TimeField()
	ter_abertura = models.TimeField()
	ter_fechamento = models.TimeField()
	qua_abertura = models.TimeField()
	qua_fechamento = models.TimeField()
	qui_abertura = models.TimeField()
	qui_fechamento = models.TimeField()
	sex_abertura = models.TimeField()
	sex_fechamento = models.TimeField()
	sab_abertura = models.TimeField()
	sab_fechamento = models.TimeField()


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
	#horario_funcionamento = models.TimeField()
	dom_abertura = models.TimeField()
	dom_fechamento = models.TimeField()
	seg_abertura = models.TimeField()
	seg_fechamento = models.TimeField()
	ter_abertura = models.TimeField()
	ter_fechamento = models.TimeField()
	qua_abertura = models.TimeField()
	qua_fechamento = models.TimeField()
	qui_abertura = models.TimeField()
	qui_fechamento = models.TimeField()
	sex_abertura = models.TimeField()
	sex_fechamento = models.TimeField()
	sab_abertura = models.TimeField()
	sab_fechamento = models.TimeField()
	
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