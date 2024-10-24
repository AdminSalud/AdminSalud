from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Paciente, Evoluciones,Profesional
from  django.contrib import messages 
import pandas as pd
import json
from django.contrib.auth import logout
from .forms import PacienteForm
from django.db.models import Q

# Create your views here.


@login_required
def home(request):
    pacienteslistados = Paciente.objects.filter(id_user = request.user.id)
    messages.success(request,'Pacientes listados')
    return render(request,"gestionpacientes.html",{"pacientes":pacienteslistados})

def gestion_pacientes(request):
    id_usuario = request.user.id
    query = request.GET.get('q')
    if query:
        pacientes = Paciente.objects.filter(
            Q(cc__icontains=query) | 
            Q(nombre__icontains=query) | 
            Q(apellidos__icontains=query),
            id_user=id_usuario
        )
    else:
        pacientes = Paciente.objects.filter(id_user=id_usuario)
    return render(request, 'gestionpacientes.html', {'pacientes': pacientes})



def exit(request):
    logout(request)
    return render(request,"registration/logout.html")

def editarPerfil(request):
    id_usuario = request.user.id
    try:
        profesional = Profesional.objects.get(id_user=id_usuario)
    except Profesional.DoesNotExist:
       return render(request, "perfil.html")
    context = {
        'Perfil': profesional,
    }
    return render(request, "perfil.html", context)


def registraperfil(request):

    id_usuario = request.user.id
    cc_profesional = request.POST['cc_profesional']
    TD_profesional = request.POST['TD_profesional']
    NombreApellidos = request.POST['NombreApellidos']
    genero = request.POST['genero']
    Email = request.POST['Email']
    direccion = request.POST['direccion']
    ciudad = request.POST['ciudad']
    tel_contacto = request.POST['tel_contacto']
    especialidad = request.POST['especialidad']
    ciudad_residencia = request.POST['ciudad_residencia']
    tel_contacto = request.POST['tel_contacto']
    horarioAtencion = request.POST['horarioAtencion']
    codigoPrestador = request.POST['tcodigoPrestador']
    
     # Manejo del archivo de exámenes clínicos
    Foto = request.FILES.get('Foto', None)  # Solo lo toma si está presente
        

    Paciente.objects.create(
    id_user = id_usuario , 
    TD_profesional = TD_profesional,
    cc_profesional= cc_profesional,
    NombreApellidos = NombreApellidos,
    genero = genero,
    Email = Email, 
    ocupacion = ocupacion, 
    direccion = direccion,
    ciudad= cciudad,
    tel_contacto = tel_contacto,
    horarioAtencion = horarioAtencion,
    codigoPrestador = codigoPrestador,
    Foto = Foto)

    messages.success(request, '¡Pacientes registrado!')
    return redirect('/')
  
def registrapaciente(request):
    
 
    id_usuario = request.user.id
    tipo_documento = request.POST['tipo_documento']
    cc = request.POST['numcc']
    nombre = request.POST['txtnombre']
    apellidos = request.POST['txtapellidos']
    genero = request.POST['genero']
    eps = request.POST['eps']
    estado_civil = request.POST['estado_civil']
    ocupacion = request.POST['ocupacion']
    direccion_domicilio = request.POST['direccion_domicilio']
    ciudad_residencia = request.POST['ciudad_residencia']
    tel_contacto = request.POST['tel_contacto']
    fechaNacimiento = request.POST['fecha_nacimiento']
    nombreAcompanante = request.POST['nombre_acompanante']
    parentesco = request.POST['parentesco']
    tel_contacto_acompanante = request.POST['tel_contacto_acompanante']
    motivoConsulta = request.POST['motivo_consulta']
    AntecedentesMedicos = request.POST['AntecedentesMedicos']
    CondicionesMedicasAct = request.POST['CondicionesMedicasAct']
    His_problemasPsicologicos = request.POST['His_problemasPsicologicos']
    His_tratamientoAnteriones = request.POST['His_tratamientoAnteriones']
    composicionFamiliar = request.POST['composicionFamiliar']
    antecedentesdeEnfermedadesMentales = request.POST['antecedentesdeEnfermedadesMentales']
    RelacionesInterpersonales = request.POST['RelacionesInterpersonales']
    ApoyoSocial = request.POST['ApoyoSocial']
    SintomasActuales = request.POST['SintomasActuales']
    objetivosdelaTerapia = request.POST['objetivosdelaTerapia']
    HistoriadeVida = request.POST['HistoriadeVida']
    evalucionDiagnosticaPreliminar = request.POST['evalucionDiagnosticaPreliminar']
    enfoqueterapeutico = request.POST['enfoqueterapeutico']
    FrecuenciadeSecciones = request.POST['FrecuenciadeSecciones']
    IntervencionesyEstrategias = request.POST['IntervencionesyEstrategias']


     # Manejo del archivo de exámenes clínicos
    Examenes_clinicos = request.FILES.get('Examenes_clinicos', None)  # Solo lo toma si está presente
        

    Paciente.objects.create(id_user = id_usuario ,  TipoDocumento = tipo_documento, cc = cc , nombre = nombre, apellidos =apellidos, genero = genero, eps = eps, estado_civil = estado_civil, ocupacion = ocupacion, 
    direccion_domicilio = direccion_domicilio, ciudad_residencia = ciudad_residencia, tel_contacto = tel_contacto, fechaNacimiento = fechaNacimiento, nombreAcompanante = nombreAcompanante, parentesco = parentesco,
     tel_contacto_acompanante = tel_contacto_acompanante, motivoConsulta = motivoConsulta, AntecedentesMedicos = AntecedentesMedicos, CondicionesMedicasAct = CondicionesMedicasAct, His_problemasPsicologicos = His_problemasPsicologicos, 
     His_tratamientoAnteriones = His_tratamientoAnteriones, composicionFamiliar = composicionFamiliar, antecedentesdeEnfermedadesMentales = antecedentesdeEnfermedadesMentales, RelacionesInterpersonales = RelacionesInterpersonales, 
     ApoyoSocial = ApoyoSocial, SintomasActuales = SintomasActuales, objetivosdelaTerapia = objetivosdelaTerapia, HistoriadeVida = HistoriadeVida, evalucionDiagnosticaPreliminar = evalucionDiagnosticaPreliminar, 
     enfoqueterapeutico = enfoqueterapeutico, FrecuenciadeSecciones = FrecuenciadeSecciones, IntervencionesyEstrategias = IntervencionesyEstrategias, Examenes_clinicos = Examenes_clinicos)
    messages.success(request, '¡Pacientes registrado!')
    return redirect('/')

def historiaclinica(request):


    return render(request, "historiaclinica.html")



def editarPaciente(request,cc):
    id_usuario = request.user.id
    paciente = Paciente.objects.get(cc=cc, id_user = id_usuario)
    context = {
        'paciente': paciente,
        'Examenes_clinicos': paciente.Examenes_clinicos.url if paciente.Examenes_clinicos else None,
    }
    return render(request, "editarPaciente.html", context)

def edicionPaciente(request):
    id_usuario = request.user.id
    cc = request.POST.get('numcc')
    eps = request.POST.get('eps')
    estado_civil = request.POST.get('estado_civil')
    ocupacion = request.POST.get('ocupacion')
    direccion_domicilio = request.POST.get('direccion_domicilio')
    ciudad_residencia = request.POST.get('ciudad_residencia')
    tel_contacto = request.POST.get('tel_contacto')
    nombre_acompanante = request.POST.get('nombre_acompanante')
    parentesco = request.POST.get('parentesco')
    tel_contacto_acompanante = request.POST.get('tel_contacto_acompanante')
    AntecedentesMedicos = request.POST.get('AntecedentesMedicos')
    CondicionesMedicasAct = request.POST.get('CondicionesMedicasAct')
    his_problemasPsicologicos = request.POST.get('His_problemasPsicologicos')
    His_tratamientoAnteriones = request.POST.get('His_tratamientoAnteriones')
    composicionFamiliar = request.POST.get('composicionFamiliar')
    antecedentesdeEnfermedadesMentales = request.POST.get('antecedentesdeEnfermedadesMentales')
    Examenes_clinicos = request.FILES.get('Examenes_clinicos', None)  # Solo lo toma si está presente
    RelacionesInterpersonales = request.POST.get('RelacionesInterpersonales')
    ApoyoSocial = request.POST.get('ApoyoSocial')
    SintomasActuales = request.POST.get('SintomasActuales')
    objetivosdelaTerapia = request.POST.get('objetivosdelaTerapia')
    HistoriadeVida = request.POST.get('HistoriadeVida')
    evalucionDiagnosticaPreliminar= request.POST.get('evalucionDiagnosticaPreliminar')
    enfoqueterapeutico = request.POST.get('enfoqueterapeutico')
    FrecuenciadeSecciones = request.POST.get('FrecuenciadeSecciones')
    IntervencionesyEstrategias = request.POST.get('IntervencionesyEstrategias')



    paciente = Paciente.objects.get(cc=cc)
    paciente.eps = eps
    paciente.estado_civil = estado_civil
    paciente.ocupacion = ocupacion
    paciente.direccion_domicilio = direccion_domicilio
    paciente.ciudad_residencia = ciudad_residencia
    paciente.tel_contacto = tel_contacto
    paciente.nombreAcompanante = nombre_acompanante
    paciente.parentesco = parentesco
    paciente.tel_contacto_acompanante = tel_contacto_acompanante
    paciente.AntecedentesMedicos = AntecedentesMedicos
    paciente.CondicionesMedicasAct = CondicionesMedicasAct
    paciente.his_problemasPsicologicos = his_problemasPsicologicos
    paciente.His_tratamientoAnteriones = His_tratamientoAnteriones
    paciente.composicionFamiliar = composicionFamiliar
    paciente.antecedentesdeEnfermedadesMentales = antecedentesdeEnfermedadesMentales
    if Examenes_clinicos:
        paciente.Examenes_clinicos = Examenes_clinicos
    paciente.RelacionesInterpersonales = RelacionesInterpersonales
    paciente.ApoyoSocial = ApoyoSocial
    paciente.SintomasActuales = SintomasActuales
    paciente.objetivosdelaTerapia = objetivosdelaTerapia
    paciente.HistoriadeVida = HistoriadeVida
    paciente.evalucionDiagnosticaPreliminar = evalucionDiagnosticaPreliminar
    paciente.enfoqueterapeutico = enfoqueterapeutico
    paciente.FrecuenciadeSecciones = FrecuenciadeSecciones
    paciente.IntervencionesyEstrategias = IntervencionesyEstrategias
    paciente.save()
    messages.success(request, 'La información del paciente ha sido editada correctamente.')
    return redirect('/')

def evoluciones(request, cc):
    id_usuario = request.user.id
    paciente = Paciente.objects.get(cc=cc, id_user = id_usuario)
    evoluciones = Evoluciones.objects.filter(cc_paciente=paciente, id_user=id_usuario)
    context = {
        'paciente': paciente,
        'evoluciones': evoluciones,
    }
    return render(request, 'evolucion.html', context)

def grabarevolucion(request,cc):
    
    paciente = get_object_or_404(Paciente, cc=cc)
    id_usuario = request.user.id
    if request.method == 'POST':
        evolucion = request.POST.get('CrearEvolucion')
        Evoluciones.objects.create(id_user=id_usuario , cc_paciente=paciente, evolucion=evolucion)
        return redirect('gestion_pacientes')  # Redirige a la página de gestión de pacientes después de guardar
    else:
        return render(request, 'crear_evolucion.html', {'paciente': paciente})



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
               "fechaNacimiento": str(row["FECHA NACIMIENTO "]),
               "nombre": str(row["Primer NOMBRE"]),
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







