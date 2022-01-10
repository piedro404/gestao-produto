from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produto
from .form import ProdutoForm
import os


@login_required
def produto_list(reguest):
    produtos = Produto.objects.all()
    return render(reguest, "produto.html", {"produtos": produtos})

@login_required
def produto_new(reguest):
    form = ProdutoForm(reguest.POST or None, reguest.FILES or None)

    if form.is_valid():
        form.save()
        return redirect("produto_list")

    return render(reguest, "produto_form.html",{"form": form})

@login_required
def produto_update(reguest, id):
    produto = get_object_or_404(Produto, pk=id)
    form = ProdutoForm(reguest.POST or None, reguest.FILES or None, instance=produto)
    foto_old = None
    if produto.foto:
        foto_old = produto.foto

    if form.is_valid():
        if foto_old:
            os.remove(f"media/{foto_old}")
        form.save()
        return redirect("produto_list")

    return render(reguest, "produto_form.html", {"form": form})

@login_required
def produto_delete(reguest, id):
    produto = get_object_or_404(Produto, pk=id)
    foto_old = None
    if produto.foto:
        foto_old = produto.foto

    if reguest.method == "POST":
        if foto_old:
            os.remove(f"media/{produto.foto}")
        produto.delete()
        return redirect("produto_list")

    return render(reguest, "produto_delete_confirm.html",{"produto": produto})