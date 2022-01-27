from django.shortcuts import redirect, render
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib import auth
import json
from django.contrib.auth.models import User
from esoftapi.models import Adress



def login(request):
    return render(request, "login.html", {})

def autenticar(request):
    email = request.POST.get("email")
    password = request.POST.get("password")
    user = auth.authenticate(username=email, password=password)

    if user is not None and user.is_active:
        request.session.set_expiry(3600)
        auth.login(request, user)
        return JsonResponse({"mensagem": "OK"})
    else:
        return JsonResponse({"mensagem": "ERRO"})

def cadastro(request):
    return render(request, "cadastro.html", {})

def salvar_cadastro(request):
    try:
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        password = request.POST.get("password")
        usuarios = User.objects.filter(email=email)
        if len(usuarios) > 0:
            return JsonResponse({"mensagem":"EXISTENTE"})
        user = User.objects.create_user(nome, email, password)
        user.save()
        endereco = Adress()
        endereco.cep = request.POST.get("cep").replace(".", "").replace("-","")
        endereco.endereço = request.POST.get("endereco")
        endereco.numero = request.POST.get("numero")
        endereco.complemento = request.POST.get("complemento")
        endereco.bairro = request.POST.get("bairro")
        endereco.cidade = request.POST.get("cidade")
        endereco.estado = request.POST.get("uf")
        endereco.id_usuario = User.objects.filter(email=email)[0]
        endereco.save()
        return JsonResponse({"mensagem":"OK"})
    except Exception as e:
        print(e)
        return JsonResponse({"mensagem":"ERRO"})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")
        