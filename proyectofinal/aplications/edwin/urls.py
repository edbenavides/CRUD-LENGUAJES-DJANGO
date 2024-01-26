from django.contrib import admin
from django.urls import path


from.import views


urlpatterns = [
    #path('activos/', views.ProyectoView.as_view()),
    path('home/', views.HomeView.as_view(),name='proyectoPrincipal'),
    path('crear/', views.ProyectoCreateView.as_view(),name='crearapli'),
    path('listar/', views.ProyectoListView.as_view(),name='proyectolistar'),
    path('listar_actualizar/', views.ProyectoActualizarListView.as_view(),name='proyectolistar_actualizar'),
    path('actualizar/<int:pk>/', views.ProyectoUpdateView.as_view(), name='proyecto_actualizar'),

    path('listar_eliminar/', views.ProyectoEliminarListView.as_view(),name='proyectolistar_eliminar'),
    path('eliminar/<int:pk>', views.ProyectoDeleteView.as_view(), name='proyecto_eliminar')



    #path('actualizar/', views.HomeView.as_view(),name='proyectoactulizar')
   
    #path('actualizar/<int:pk>/', views.pruebaUpdateView.as_view(), name='actualizar'),
]
