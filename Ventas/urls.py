from django.urls import path
from.import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('informacion', views.informacion, name='informacion'),
    #####################################################################################
    path('Clientes', views.Clientes, name='Clientes'),
    path('Clientes/Crear', views.Crear_Clientes, name='Crear'),
    path('Clientes/editar/<str:numero>/', views.Editar_Clientes, name='Editar'),
    path('Clientes/eliminar/<str:numero>/', views.Eliminar_Clientes, name='Eliminar'),
    ######################################################################################
    path('Facturas', views.Facturas, name='Facturas'),
    path('Facturas/idear', views.Idear_Facturas, name='Idear'),
    path('Facturas/revisar/<str:numero>/', views.Revisar_Facturas, name='Revisar'),
    path('Facturas/quitar/<str:numero>/', views.Quitar_Facturas, name='Quitar'),
    #######################################################################################
    path('Productos', views.Productos, name='Productos'),
    path('Productos/fundar', views.Fundar_Productos, name='Fundar'),
    path('Productos/corregir/<str:numero>/', views.Corregir_Productos, name='Corregir'),
    path('Productos/excluir/<str:numero>/', views.Excluir_Productos, name='Excluir'),
    #######################################################################################
    path('Reportes', views.reportes, name='Reportes'),
]
