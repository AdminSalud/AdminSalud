from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Paciente
from  django.contrib import messages 
import pandas as pd
import json
from django.contrib.auth import logout


# Create your views here.


@login_required
def home(request):
    pacienteslistados = Paciente.objects.filter(id_user = request.user.id)
    messages.success(request,'Pacientes listados')
    return render(request,"gestionpacientes.html",{"pacientes":pacienteslistados})


def exit(request):
    logout(request)
    return render(request,"registration/logout.html")
  
def registrapaciente(request):
    id_usuario = request.user.id
    cc = request.POST['numcc']
    nombre = request.POST['txtnombre']
    historiaclinica = request.POST['txthistoriaclinica']

    Paciente.objects.create(id_user = id_usuario ,cc = cc, nombre = nombre, historiaclinica = historiaclinica)
    messages.success(request, '¡Pacientes registrado!')
    return redirect('/')


def editarPaciente(request,cc):
    paciente = Paciente.objects.get(cc=cc)
    return render (request,"editarPaciente.html", {"paciente":paciente})    

def edicionPaciente(request):
    
    cc = request.POST['numcc']
    nombre = request.POST['txtnombre']
    historiaclinica = request.POST['txthistoriaclinica']

    paciente = Paciente.objects.get(cc=cc)
    paciente.nombre = nombre
    paciente.historiaclinica = historiaclinica
    paciente.save()
    return redirect('/')

def eliminarPaciente(request,cc):
    paciente = Paciente.objects.get(cc=cc)
    paciente.delete()

    return redirect('/')
def mostrar_registro(request):
    return render(request,'register.html')

def mostrar_validador(request):
    return render(request, 'Validador.html')

def mostrar_home(request):
    return render(request,'gestionpacientes.html')

def pasarjson(request):
    ruta = request.FILES['excel_file']
    datapath = ruta
    outpath = r"C:\Users\Usuario\Desktop\pruebas JSON\prueba.json"

    data= pd.read_excel(datapath)
    print(data.columns)
    
    

    container = {
        "numDocumentoIdObligado": "",
        "numFactura": "",
        "tipoNota": "",
        "numNota": "",
        "usuarios": []
    }

    for index, row in data.iterrows():
        tipo_usuario = str(row["TIPO USUARIO AFILIACION"])
        if tipo_usuario == "" or pd.isnull(tipo_usuario):
            tipo_usuario = ""
        usuario = {
               "tipoDocumentoIdentificacion": str(row["Tipo de Identific. del Usuario"]),
               "tipoUsuario": tipo_usuario,
               "fechaNacimiento": str(row["FECHA NACIMIENTO "])
        }
        container["usuarios"].append(usuario)

    

   # json_data = json.dumps(container, indent=2)

    with open(outpath, "w") as file:
      json.dump(container, file, indent=2)
   # df = pd.DataFrame (container)
    #df.to_json(outpath, indent=2)
   # print (df)
    
   # print(json_data)


    return redirect(mostrar_validador)







