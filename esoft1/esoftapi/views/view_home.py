from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from esoftapi.models import Produto

def home(request):
    if request.user.is_authenticated:
        qtd_produtos = Produto.objects.all().count()    
        return render(request, "home.html", {"qtd_produtos":qtd_produtos})
    return HttpResponseRedirect("/login")