from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home (request):
    return render(request, 'home.html')

def detalle (request):
    return render(request, 'detalle.html')

# Datos de la ES1: copia esta lista completa dentro de carta/views.py
# No cambies los nombres de las claves ni los tipos de dato.

#PLATOS = [
    {"id": 1, "nombre": "Ceviche de reineta", "categoria": "Entrada", "precio": 8900,
     "tiempo": 10, "picante": True, "vegetariano": False,
     "descripcion": "Reineta fresca marinada en limon con cebolla morada, cilantro y aji verde."},
    {"id": 2, "nombre": "Empanadas de queso", "categoria": "Entrada", "precio": 4500,
     "tiempo": 15, "picante": False, "vegetariano": True,
     "descripcion": "Tres empanadas fritas de masa casera rellenas con queso mantecoso."},
    {"id": 3, "nombre": "Caldillo de congrio", "categoria": "Fondo", "precio": 12900,
     "tiempo": 25, "picante": False, "vegetariano": False,
     "descripcion": "Congrio dorado en caldo de verduras, papas y vino blanco. Receta de la casa."},
    {"id": 4, "nombre": "Pastel de choclo", "categoria": "Fondo", "precio": 9900,
     "tiempo": 30, "picante": False, "vegetariano": False,
     "descripcion": "Pino de carne, pollo, huevo y aceitunas cubierto con pasta de choclo gratinada."},
    {"id": 5, "nombre": "Porotos granados", "categoria": "Fondo", "precio": 7900,
     "tiempo": 20, "picante": False, "vegetariano": True,
     "descripcion": "Porotos frescos con zapallo, choclo y albahaca. Plato de temporada."},
    {"id": 6, "nombre": "Chorrillana", "categoria": "Fondo", "precio": 11900,
     "tiempo": 20, "picante": True, "vegetariano": False,
     "descripcion": "Papas fritas con carne salteada, cebolla, huevo y aji verde. Para compartir."},
    {"id": 7, "nombre": "Leche asada", "categoria": "Postre", "precio": 3900,
     "tiempo": 5, "picante": False, "vegetariano": True,
     "descripcion": "Postre tradicional de leche, huevo y caramelo, horneado y servido frio."},
    {"id": 8, "nombre": "Mote con huesillo", "categoria": "Postre", "precio": 2900,
     "tiempo": 5, "picante": False, "vegetariano": True,
     "descripcion": "Duraznos deshidratados cocidos en almibar con mote de trigo. Se sirve helado."},
#]
