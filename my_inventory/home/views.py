from django.shortcuts import render
from django.db.models import Q
from product.models import Product
from employee.models import Employee
from costomer.models import Costomer

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
        query = Q(name_emp=search_param)
        query.add(Q(code_emp=search_param), Q.OR)
        employees = Employee.objects.filter(query)
        context_dict.update(
            {
                "employees": employees,
                "search_param":search_param,
            }
        )
        query = Q(name_cost=search_param)
        query.add(Q(code_cost=search_param), Q.OR)
        costomers = Costomer.objects.filter(query)
        context_dict.update(
            {
                "costomers": costomers,
                "search_param":search_param,
            }
        )
    return render(
        request=request,
        context=context_dict,
        template_name="home/index.html",
    )