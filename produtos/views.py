from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produto
from .form import ProdutoForm


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

    if form.is_valid():
        form.save()
        return redirect("produto_list")

    return render(reguest, "produto_form.html", {"form": form})

@login_required
def produto_delete(reguest, id):
    produto = get_object_or_404(Produto, pk=id)

    if reguest.method == "POST":
        produto.delete()
        return redirect("produto_list")

    return render(reguest, "produto_delete_confirm.html",{"produto": produto})