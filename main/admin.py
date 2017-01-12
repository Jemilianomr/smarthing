from django.contrib import admin
from .models import Producto

class ProAdmin(admin.ModelAdmin):
	list_display = ('titulo','slug')
	search_fields = ('titulo','cuerpo')
	prepopulated_fields = {'slug':('titulo',)}

admin.site.register(Producto, ProAdmin)


# Register your models here.
