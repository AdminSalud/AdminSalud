from django.db import models

# Create your models here.
class Paciente(models.Model):
    class TipoDocumentoChoices(models.TextChoices):
        CC = 'CC', 'Cédula de Ciudadanía'
        CE = 'CE', 'Cédula de Extranjería'        
        TI = 'TI', 'Tarjeta de Identidad'
        RC = 'RC', 'Registro Civil'
        PA = 'PA', 'Pasaporte'
    
      # Lista de ciudades de Colombia
    CIUDADES_COLOMBIA = [
        ('Bogotá', 'Bogotá'),
        ('Medellín', 'Medellín'),
        ('Cali', 'Cali'),
        ('Barranquilla', 'Barranquilla'),
        ('Cartagena', 'Cartagena'),
        ('Cúcuta', 'Cúcuta'),
        ('Bucaramanga', 'Bucaramanga'),
        ('Pereira', 'Pereira'),
        ('Santa Marta', 'Santa Marta'),
        ('Ibagué', 'Ibagué'),
        # Añade más ciudades según sea necesario
    ]
    id_user = models.IntegerField(default=0)
    cc = models.IntegerField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=100, null=False)
    apellidos = models.CharField(max_length=100, null=False)
    genero = models.CharField(max_length=10, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')], null=False)
    eps = models.CharField(max_length=100)
    estado_civil = models.CharField(max_length=50)
    ocupacion = models.CharField(max_length=100)
    direccion_domicilio = models.CharField(max_length=200, null=False)
    ciudad_residencia = models.CharField(max_length=100, choices=CIUDADES_COLOMBIA, null=False)
    tel_contacto = models.CharField(max_length=20, null=False)
    TipoDocumento = models.CharField(
        max_length=2,
        choices=TipoDocumentoChoices.choices,
        default=TipoDocumentoChoices.CC
    )
    fechaNacimiento = models.DateField(default='2000-01-01')
    nombreAcompanante = models.CharField(max_length=150, default='')
    parentesco = models.CharField(max_length=50, default='')
    tel_contacto_acompanante = models.CharField(max_length=20, default='')
    motivoConsulta = models.TextField(default='', null=False)
    AntecedentesMedicos = models.TextField(default='')
    CondicionesMedicasAct = models.TextField(default='')
    His_problemasPsicologicos = models.TextField(default='')
    His_tratamientoAnteriones = models.TextField(default='')
    composicionFamiliar = models.TextField(default='')
    antecedentesdeEnfermedadesMentales = models.TextField(default='')
    RelacionesInterpersonales = models.TextField(default='')
    ApoyoSocial = models.TextField(default='')
    SintomasActuales = models.TextField(default='')
    objetivosdelaTerapia = models.TextField(default='')
    HistoriadeVida = models.TextField(default='')
    evalucionDiagnosticaPreliminar = models.TextField(default='')
    enfoqueterapeutico = models.TextField(default='')
    FrecuenciadeSecciones = models.TextField(default='')
    IntervencionesyEstrategias = models.TextField(default='')
    fechaCreacion = models.DateTimeField(auto_now_add=True, null=False)
    num_historiaclinica = models.IntegerField(default=0,max_length=6)
    # Campo para subir imágenes o archivos PDF
    Examenes_clinicos = models.FileField(upload_to='archivos_clinicos/', null=True, blank=True)
    
     # Sobrescribir el método save() para generar el número de historia clínica
    def save(self, *args, **kwargs):

        # Lógica para el número de historia clínica
        if not self.num_historiaclinica:  # Solo asignar el número si no tiene uno asignado
            ultimo_paciente = Paciente.objects.filter(id_user=self.id_user).order_by('-num_historiaclinica').first()
            
            if ultimo_paciente:
                self.num_historiaclinica = ultimo_paciente.num_historiaclinica + 1
            else:
                self.num_historiaclinica = 1  # Si no hay pacientes, iniciar con 1

        # Llamar al método save de la clase padre para guardar el registro
        super(Paciente, self).save(*args, **kwargs)
    

    def __str__(self):
        texto = "{0} - {1}"
        return texto.format(self.cc, self.nombre)




class Evoluciones(models.Model):
    
    cc_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    id_user = models.IntegerField(default=0)
    fecha = models.DateTimeField(auto_now_add=True)
    evolucion = models.TextField()

    
    def __str__(self):
        texto = "{0} - {1}"
        return texto.format(self.paciente.cc, self.fecha)


class Profesional(models.Model):
    id_user = models.IntegerField(default=0)
    TD_profesional = models.CharField(max_length=2, choices=[('CC', 'Cédula de Ciudadanía'), ('CE', 'Cédula de Extranjería'), ('TI', 'Tarjeta de Identidad'), ('RC', 'Registro Civil'), ('PA', 'Pasaporte')], null=False)
    cc_profesional = models.IntegerField(primary_key=True, max_length=15)   
    NombreApellidos  = models.CharField(max_length=254, null=False)
    Foto = models.ImageField(upload_to='fotos_profesionales/', null=True, blank=True)
    Email: models.EmailField(max_length=254, null=False)
    genero = models.CharField(max_length=10, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')], null=False)
    direccion = models.CharField(max_length=200, null=False)
    Profesion  = models.CharField(max_length=200, null=False)
    ciudad = models.CharField(max_length=100, null=False)
    tel_contacto = models.CharField(max_length=20, null=False)
    especialidad = models.CharField(max_length=100)
    horarioAtencion = models.CharField(max_length=100)
    codigoPrestador = models.IntegerField(default=0)
    
    def __str__(self):
        texto = "{0} - {1}"
        return texto.format(self.cc, self.nombre)
