from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/cadastrar/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('clientes/excluir/<int:cliente_id>/', views.excluir_cliente, name='excluir_cliente'),
    path('clientes/excluir_selecionados/', views.excluir_clientes_selecionados, name='excluir_clientes_selecionados'),


   
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('produtos/cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
    path('produtos/excluir/<int:produto_id>/', views.excluir_produto, name='excluir_produto'),
    path('produtos/excluir_selecionados/', views.excluir_produtos_selecionados, name='excluir_produtos_selecionados'),


   
    path('vendas/', views.lista_vendas, name='lista_vendas'),
    path('vendas/cadastrar/', views.cadastrar_venda, name='cadastrar_venda'),
    path('vendas/excluir/<int:venda_id>/', views.excluir_venda, name='excluir_venda'),
    path('vendas/excluir_selecionados/', views.excluir_vendas_selecionadas, name='excluir_vendas_selecionadas'),

]
