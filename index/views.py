from django.shortcuts import render

def index(request):
    return render(request, 'index/index.html', {})

def plantilla(request):
    datos= {
        'lista': ['primero', 'segundo', 'tercero'],
        'nombre': 'Ema',
        'apellido': 'Farcy'
    }
    return render(request, 'index/plantilla.html', datos)