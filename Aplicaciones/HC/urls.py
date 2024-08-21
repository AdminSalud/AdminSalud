from django.urls import path
from . import views 

urlpatterns = [
    path ('',views.home),
    path ('registrapaciente/',views.registrapaciente),
    path ('editarPaciente/<cc>',views.editarPaciente),
    path ('edicionPaciente/',views.edicionPaciente),
    path ('eliminarPaciente/<cc>',views.eliminarPaciente),
    path ('Validador.html', views.mostrar_validador, name='mostrar_validador'),
    path ('register.html',views.mostrar_registro, name='mostrar_registro'), 
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path ('pasarjson/',views.pasarjson )

]


