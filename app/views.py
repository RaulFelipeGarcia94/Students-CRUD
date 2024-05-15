import re
from django.shortcuts import render, redirect
from django.utils.datetime_safe import datetime
from .models import Student
from django.contrib import messages

def index(request):
    data = Student.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)

def insertData(request):
    if request.method == "POST":
        matricula = request.POST.get('registration')
        email = request.POST.get('email')
        data_nascimento_str = request.POST.get('birth')
        telefone = request.POST.get('phone')
        data_ingresso_str = request.POST.get('initial')

        data_nascimento = datetime.strptime(data_nascimento_str, '%d/%m/%Y').date()
        data_ingresso = datetime.strptime(data_ingresso_str, '%d/%m/%Y').date()

        student = Student.objects.create(
            matricula=matricula,
            email=email,
            data_nascimento=data_nascimento,
            telefone=telefone,
            data_ingresso=data_ingresso
        )
        messages.info(request,"Usuário inserido com sucesso!" )
        return redirect("/")

    return render(request, "index.html")

def updateData(request, id):
    if request.method == "POST":
        matricula = request.POST.get('registration')
        email = request.POST.get('email')
        data_nascimento_str = request.POST.get('birth')
        telefone = request.POST.get('phone')
        data_ingresso_str = request.POST.get('initial')

        data_nascimento = datetime.strptime(data_nascimento_str, '%d/%m/%Y').date()
        data_ingresso = datetime.strptime(data_ingresso_str, '%d/%m/%Y').date()

        student = Student.objects.get(id=id)
        student.matricula = matricula
        student.email = email
        student.data_nascimento = data_nascimento
        student.telefone = telefone
        student.data_ingresso = data_ingresso
        student.save()
        messages.warning(request,"Usuário editado com sucesso!" )
        return redirect("/")

    d = Student.objects.get(id=id)
    
    # Formatando as datas antes de passá-las para o contexto
    d.data_nascimento = d.data_nascimento.strftime('%d/%m/%Y')
    d.data_ingresso = d.data_ingresso.strftime('%d/%m/%Y')
    
    context = {"d": d}
    return render(request, "edit.html", context)


def deleteData(request, id):
    d=Student.objects.get(id=id)
    d.delete()
    messages.error(request,"Usuário deletados com sucesso!" )
    return redirect("/")
    

def about(request):
    return render(request, "about.html")
