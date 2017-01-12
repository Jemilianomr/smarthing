from django.shortcuts import render
from django.views.generic import View
from .models import Producto

class HomeView(View):
	def get(self, request):
		template_name = 'home.html'
		return render(request,template_name)
		

class PrinView(View):
	def get(self,request):
		template_name='pro.html'
		productos = Producto.objects.all()
		cuerpo = {
			'productos':productos,
			}	
		return render(request,template_name,cuerpo)

class ProView(View):
	def get(self,request,slug):
		template_name = 'detalle.html'
		producto = Producto.objects.get(slug=slug)
		context = {
		'producto':producto,
		}
		return render(request,template_name,context)
		

# Create your views here.
