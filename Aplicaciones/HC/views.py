from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Paciente
from  django.contrib import messages 
import pandas as pd
import json



# Create your views here.
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        # Puedes personalizar esta redirección según tus necesidades
        return redirect('/')
    else:
        return render(request, 'register.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        # Puedes personalizar esta redirección según tus necesidades
        return redirect('/')
    else:
        return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirigir a la página de inicio o a otra página deseada
            return redirect('/')
        else:
            # Mostrar un mensaje de error de inicio de sesión
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    # Redirigir a la página de inicio o a otra página deseada
    return redirect('/')

def home(request):
    pacienteslistados = Paciente.objects.all()
    messages.success(request,'Pacientes listados')
    return render(request,"gestionpacientes.html",{"pacientes":pacienteslistados})
    """
   # if request.method == 'POST':
     #   username = request.POST['username']
      #  password = request.POST['password']
       # user = authenticate(request, username=username, password=password)
       # if user is not None:
            login(request, user)
                # Redirigir a la página de inicio o a otra página deseada
            return redirect('/')
        else:
                # Mostrar un mensaje de error de inicio de sesión
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login.html')
    """



def registrapaciente(request):
    cc = request.POST['numcc']
    nombre = request.POST['txtnombre']
    historiaclinica = request.POST['txthistoriaclinica']

    Paciente.objects.create(cc = cc, nombre = nombre, historiaclinica = historiaclinica)
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







