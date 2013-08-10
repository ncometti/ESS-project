from django.shortcuts import HttpResponse, render
from models import Restaurante, Comentario


def home(request):
	return render(request, 'Home.html')

def paris(request):
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