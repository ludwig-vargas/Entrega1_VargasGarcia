from django.shortcuts import render

# Muestra el Index de home
def index(request):
    return render (
    request = request,
    context = {},
    template_name = 'home/index.html',     
    )