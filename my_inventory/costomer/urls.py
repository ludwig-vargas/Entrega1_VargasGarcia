from django.urls import path
from costomer import views

app_name = 'costomer'
urlpatterns = [
    path('costomers/', views.CostomerListView.as_view(), name='costomer-list'),
    path('costomer/add/', views.CostomerCreateView.as_view(), name='costomer-add'),
]