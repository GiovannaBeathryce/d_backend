from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadForm
from .models import Financial_control
from rest_framework.views import APIView
from django.forms.models import model_to_dict
from datetime import datetime


def handle_uploaded_file(f):
    file = f.readlines()

    for row in file:
        tipo = row[0:1].decode()

        data = row[1:9].decode()
        date = datetime.strptime(data, "%Y%m%d").date()

        valor = int(row[9:19].decode()) / 100

        cpf = row[19:30].decode()

        cartão = row[30:42].decode()

        hora = row[42:48]
        x_fill = str(hora).zfill(6)
        n_hora = str(x_fill)[2:4] + ":" + str(x_fill)[4:6] + ":" + str(x_fill)[6:]

        dono_da_loja = row[48:62].decode()
        n_dono_da_loja = dono_da_loja.strip()

        nome_loja = row[62:81].decode()
        n_nome_loja = nome_loja.strip()

        file = Financial_control(
            tipo=tipo,
            data=date,
            valor=valor,
            cpf=cpf,
            cartão=cartão,
            hora=str(n_hora),
            dono_da_loja=n_dono_da_loja,
            nome_loja=n_nome_loja,
        )
        file.save()


def Upload_files(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES["file"])
            return HttpResponseRedirect("/list")
    elif request.method == "GET":
        form = UploadForm()
    return render(request, "home.html", {"form": form})


class ControlViews(APIView):
    def get(self, request):
        files = Financial_control.objects.all()
        files_dict = []

        for file in files:
            f = file.nome_loja
            if not f in files_dict:
                files_dict.append(f)

        return render(request, "companies.html", {"dict": files_dict})


class CompaniesViews(APIView):
    def get(self, request, nome_loja):
        files = Financial_control.objects.all()
        list = [file for file in files if file.nome_loja == nome_loja]

        valor = 0
        
        for file in list:
            proprietario = file.dono_da_loja
            f = file.valor
            if file.tipo == 2 or file.tipo == 3 or file.tipo == 9:
                valor -= f
            else:
                valor += f
        
        return render(
            request,
            "list_files.html",
            {"nome": nome_loja, "dict": list, "valor": valor, "proprietario":proprietario},
        )
