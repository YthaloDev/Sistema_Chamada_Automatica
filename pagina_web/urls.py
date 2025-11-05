from django.urls import path

from . import views

app_name = 'pagina_web'

urlpatterns = [
    path("", views.index, name="index"),
    path("/qrcode", views.qrcode, name="qrcode"),
    path('/gerar_qrcode', views.gerar_qrcode, name='gerar_qrcode'),
    path("/chamada", views.chamada, name="chamada"),
    path("/configuracao", views.configuracao, name="configuracao"),
    
]
