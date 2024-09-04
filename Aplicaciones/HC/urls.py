from django.urls import path, include
from . import views 

urlpatterns = [
    path ('',views.home,name='home'),
    path ('registrapaciente/',views.registrapaciente),
    path ('editarPaciente/<cc>',views.editarPaciente),
    path ('edicionPaciente/',views.edicionPaciente),
    path ('eliminarPaciente/<cc>',views.eliminarPaciente),
    path ('Validador.html', views.mostrar_validador, name='mostrar_validador'),
    path ('register.html',views.mostrar_registro, name='mostrar_registro'), 
    path ('pasarjson/',views.pasarjson ),
    path ('accounts/', include('django.contrib.auth.urls')),
    path ('logout/',views.exit, name='exit'),

]


