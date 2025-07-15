from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Produto, Venda, ItemVenda
from django.contrib import messages


def home(request):
    return render(request, 'meuapp/home.html')


def cadastrar_cliente(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        telefone = request.POST['telefone']
        endereco = request.POST['endereco']

        Cliente.objects.create(
            nome=nome,
            email=email,
            telefone=telefone,
            endereco=endereco
        )
        return redirect('lista_clientes')

    return render(request, 'meuapp/cadastrar_cliente.html')


def excluir_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    cliente.delete()
    return redirect('lista_clientes')


def excluir_clientes_selecionados(request):
    if request.method == 'POST':
        ids = request.POST.getlist('clientes_ids')
        if ids:
            Cliente.objects.filter(id__in=ids).delete()
            messages.success(request, f'{len(ids)} clientes excluídos com sucesso.')
        else:
            messages.warning(request, 'Nenhum cliente selecionado para exclusão.')
    return redirect('lista_clientes')


def lista_clientes(request):
    busca = request.GET.get('busca', '').strip()
    clientes = Cliente.objects.all()

    if busca:
        clientes = clientes.filter(nome__icontains=busca)

    context = {
        'clientes': clientes,
        'busca': busca,
    }
    return render(request, 'meuapp/lista_clientes.html', context)


def cadastrar_produto(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        descricao = request.POST['descricao']
        preco = request.POST['preco']
        estoque = request.POST['estoque']

        Produto.objects.create(
            nome=nome,
            descricao=descricao,
            preco=preco,
            estoque=estoque,
        )
        return redirect('lista_produtos')

    return render(request, 'meuapp/cadastrar_produto.html')


def excluir_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    produto.delete()
    return redirect('lista_produtos')


def excluir_produtos_selecionados(request):
    if request.method == 'POST':
        ids = request.POST.getlist('produtos_ids')
        if ids:
            Produto.objects.filter(id__in=ids).delete()
            messages.success(request, f'{len(ids)} produto(s) excluído(s) com sucesso.')
        else:
            messages.warning(request, 'Nenhum produto selecionado para exclusão.')
    return redirect('lista_produtos')


def lista_produtos(request):
    busca = request.GET.get('busca', '').strip()
    estoque_min = request.GET.get('estoque_min', '').strip()

    produtos = Produto.objects.all()

    if busca:
        produtos = produtos.filter(nome__icontains=busca)

    if estoque_min:
        try:
            estoque_min_valor = int(estoque_min)
            produtos = produtos.filter(estoque__gte=estoque_min_valor)
        except ValueError:
            pass  # Valor inválido, ignora

    context = {
        'produtos': produtos,
        'busca': busca,
        'estoque_min': estoque_min,
    }
    return render(request, 'meuapp/lista_produtos.html', context)


def cadastrar_venda(request):
    if request.method == 'POST':
        cliente_id = request.POST['cliente']
        cliente = Cliente.objects.get(id=cliente_id)

        venda = Venda.objects.create(cliente=cliente, total=0)
        total_venda = 0

        produtos_ids = request.POST.getlist('produtos')
        quantidades = request.POST.getlist('quantidades')

        for produto_id, quantidade in zip(produtos_ids, quantidades):
            produto = Produto.objects.get(id=produto_id)
            quantidade = int(quantidade)

            if produto.estoque < quantidade:
                messages.error(request, f'Estoque insuficiente para o produto "{produto.nome}".')
                venda.delete()
                return redirect('cadastrar_venda')

            preco_unitario = produto.preco
            subtotal = preco_unitario * quantidade

            ItemVenda.objects.create(
                venda=venda,
                produto=produto,
                quantidade=quantidade,
                preco_unitario=preco_unitario
            )

            produto.estoque -= quantidade
            produto.save()

            total_venda += subtotal

        venda.total = total_venda
        venda.save()

        return redirect('lista_vendas')

    clientes = Cliente.objects.all()
    produtos = Produto.objects.all()
    return render(request, 'meuapp/cadastrar_venda.html', {'clientes': clientes, 'produtos': produtos})


def excluir_venda(request, venda_id):
    venda = get_object_or_404(Venda, id=venda_id)
    venda.delete()
    return redirect('lista_vendas')


def excluir_vendas_selecionadas(request):
    if request.method == 'POST':
        ids = request.POST.getlist('vendas_ids')
        if ids:
            Venda.objects.filter(id__in=ids).delete()
            messages.success(request, f'{len(ids)} venda(s) excluída(s) com sucesso.')
        else:
            messages.warning(request, 'Nenhuma venda selecionada para exclusão.')
    return redirect('lista_vendas')


def lista_vendas(request):
    busca_cliente = request.GET.get('busca_cliente', '').strip()

    vendas = Venda.objects.prefetch_related('itens', 'itens__produto').order_by('-id')

    if busca_cliente:
        vendas = vendas.filter(cliente__nome__icontains=busca_cliente)

    context = {
        'vendas': vendas,
        'busca_cliente': busca_cliente,
    }
    return render(request, 'meuapp/lista_vendas.html', context) 