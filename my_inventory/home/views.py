from django.shortcuts import render
from django.db.models import Q
from product.models import Product

# Muestra el Index de home
def index(request):
    return render (
    request = request,
    context = {},
    template_name = 'home/index.html',     
    )

def search(request):
    search_param = request.GET["search_param"]
    print("search: ", search_param)
    context_dict = dict()
    if search_param:
        query = Q(name_product=search_param)
        query.add(Q(code_product=search_param), Q.OR)
        products = Product.objects.filter(query)
        context_dict.update(
            {
                "products": products,
                "search_param": search_param,
            }
        )
    return render(
        request=request,
        context=context_dict,
        template_name="home/index.html",
    )