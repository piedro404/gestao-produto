from django.urls import path
from .views import produto_list,produto_new,produto_update,produto_delete

urlpatterns = [
    path('lista/', produto_list, name="produto_list"),
    path('new/', produto_new, name="produto_new"),
    path('update/<int:id>/', produto_update, name="produto_update"),
    path('delete/<int:id>/', produto_delete, name="produto_delete"),

]
