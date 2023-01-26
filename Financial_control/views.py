from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import UploadForm
from .models import Financial_control


def handle_uploaded_file(f):
    file = f.readlines()

    for row in file:
        file = Financial_control(
            tipo=row[0:1].decode(),
            data=row[1:9].decode(),
            valor=int(row[9:19].decode()) / 100,
            cpf=row[19:30].decode(),
            cartão=row[30:42].decode(),
            hora=row[42:48].decode(),
            dono_da_loja=row[48:62].decode(),
            nome_loja=row[62:81].decode(),
        )
        file.save()


def Upload_files(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES["file"])
            return HttpResponse("File uploaded successfuly")
    else:
        form = UploadForm()
    return render(request, "home.html", {"form": form})
