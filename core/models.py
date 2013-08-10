from django.db import models

# Create your models here.
class Restaurante(models.Model):
	nome = models.CharField(max_length=100)
	descricao = models.TextField()
	# foto = models.ImageField() # tem que instalar o PIL
	preco_medio = models.FloatField()
	qualidade = models.FloatField()

	data_cadastro = models.DateTimeField(auto_now_add=True)
	# horario_funcionamento = models.DateTimeField()
	#seg_abertura = models.TimeField()
	#seg_fechamento = models.TimeField()

	def __unicode__(self):
		return self.nome


class Comentario(models.Model):
	autor = models.CharField(max_length=100)
	conteudo = models.TextField()
	restaurante = models.ForeignKey('Restaurante')