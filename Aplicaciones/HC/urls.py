from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views 

urlpatterns = [
    path ('',views.home,name='home'),
    path ('registrapaciente/',views.registrapaciente ,name='registrapaciente'),
    path ('editarPaciente/<cc>',views.editarPaciente),
    path ('edicionPaciente/',views.edicionPaciente),
    path ('eliminarPaciente/<cc>',views.eliminarPaciente),
    path ('Validador.html', views.mostrar_validador, name='mostrar_validador'),
    path ('register.html',views.mostrar_registro, name='mostrar_registro'), 
    path ('pasarjson/',views.pasarjson ),
    path ('accounts/', include('django.contrib.auth.urls')),
    path ('logout/',views.exit, name='exit'),
    path ('historiaclinica/',views.historiaclinica, name='historiaclinica'),
    path ('gestion_pacientes/', views.gestion_pacientes, name='gestion_pacientes'),
    path ('gestion_pacientes/editarPaciente/<int:cc>/', views.editarPaciente, name='editar_paciente'),
    path ('evoluciones/<int:cc>/', views.evoluciones, name='evoluciones'),
    path ('grabarevolucion/<int:cc>/', views.grabarevolucion, name='grabarevolucion'),
    path ('registraperfil/', views.registraperfil, name='registraperfil'),
    path ('editarPerfil/', views.editarPerfil, name='editarPerfil'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


