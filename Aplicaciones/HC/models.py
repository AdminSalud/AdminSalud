from django.db import models

# Create your models here.
class Paciente(models.Model):
    id_user= models.IntegerField(default=0)
    cc=models.CharField(primary_key=True,max_length=10) 
    nombre=models.CharField(max_length=50)
    historiaclinica=models.TextField()

    def __str__(self):
        texto = "{0} - {1}"
        return texto.format(self.cc, self.nombre)