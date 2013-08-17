from django.shortcuts import HttpResponse, render
from models import Restaurante, Comentario, Evento


def home(request):
	return render(request, 'Home.html')

def paris(request):
	restaurantes = Restaurante.objects.all().order_by('-data_cadastro')
	return render(request, 'Paris.html', locals())

def paris_restaurantes(request):
	restaurantes = Restaurante.objects.all().order_by('-data_cadastro')
	return render(request, 'Paris.html', locals())

def paris_restaurante(request, restaurante_id):
	restaurante = Restaurante.objects.get(id=restaurante_id)

	if request.method == 'POST':
		comentario = Comentario()
		comentario.autor = request.POST.get('autor')
		comentario.descricao = request.POST.get('descricao')
		comentario.restaurante = restaurante
		comentario.save()

	comentarios = Comentario.objects.filter(restaurante_id=restaurante.id)

	return render(request, 'Restaurante_detalhe.html', locals())

def cronograma(request):
	return render(request, 'Cronograma.html')

def dicas(request):
	return render(request, 'Dicas.html')

def cronograma_dias(request):
	return render(request, 'Dias.html')

def ver_cronograma(request):
	return render(request, 'VerCronograma.html')

def paris_eventos(request):
	return render(request, 'Eventos.html')

def paris_diversao(request):
	return render(request, 'Diversao.html')	

def primeirosPassos(request):
	return render(request, 'PrimeirosPassos.html')	

def adicionarRestaurante(request):
	return render(request, 'AdicionarRestaurante.html')

def adicionarDiversao(request):
	return render(request, 'AdicionarDiversao.html')

def adicionarEvento(request):
	return render(request, 'AdicionarEvento.html')		