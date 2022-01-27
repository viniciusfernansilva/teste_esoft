from tkinter import EXCEPTION
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, JsonResponse
from esoftapi.models import Produto

def produtos(request):
    if request.user.is_authenticated:
        ordem = ['nome', '-preco', '-estoque']
        lista_produtos = Produto.objects.all().order_by(*ordem)
        qtd_produtos = Produto.objects.all().count()   
        return render(request, "produto.html", {"lista_produtos":lista_produtos, "qtd_produtos":qtd_produtos})
    return HttpResponseRedirect("/login")

def salvar_produto(request):
    if request.user.is_authenticated:
        try:
            nome = request.POST.get("nome")
            preco = request.POST.get("preco")
            estoque = request.POST.get("estoque")
            id_produto = request.POST.get("id")
            if id_produto == "":
                produto = Produto.objects.filter(nome=nome, preco=preco, estoque=estoque)
                if len(produto) > 0:
                    return JsonResponse({"mensagem":"EXISTENTE"})
                produto = Produto()
                produto.nome = nome
                produto.preco = preco
                produto.estoque = estoque
                produto.save()
            else:
                produto = Produto()
                produto.id = id_produto
                produto.nome = nome
                produto.preco = preco
                produto.estoque = estoque
                produto.save()         
            return JsonResponse({"mensagem":"OK"})
        except Exception as e:
            print(e)
            return JsonResponse({"mensagem":"ERRO"})
    return HttpResponseRedirect("/login")

def get_produto(request):
    if request.user.is_authenticated:
        try:
            id_produto = request.GET.get("id_produto")
            produto = Produto.objects.filter(id=id_produto).values()
            produto = list(produto)[0]
            return JsonResponse({"mensagem":"OK", "produto":produto})
        except Exception as e:
            print(e)
            return JsonResponse({"mensagem":"ERRO"})
    return HttpResponseRedirect("/login")

def del_produto(request):
    if request.user.is_authenticated:
        try:
            id_produto = request.GET.get("id_produto")
            produto = Produto.objects.filter(id=id_produto)[0]
            produto.delete()
            return JsonResponse({"mensagem":"OK"})
        except Exception as e:
            print(e)
            return JsonResponse({"mensagem":"ERRO"})
    return HttpResponseRedirect("/login")
