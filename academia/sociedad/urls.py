
from django.urls import path, include
from sociedad.views import * 


urlpatterns = [

    path('',home, name="home"),
    path('pilotos/',pilotos, name="pilotos"),
    path('autos/',autos , name="autos"),
    path('tiempos/',tiempos, name="tiempos"),
    path('posiciones/' ,posiciones, name="posiciones"),
]
