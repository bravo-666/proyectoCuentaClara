from django.urls import path
from django.views.generic import TemplateView
from backend.core.views import login_view



urlpatterns = [
    path('', TemplateView.as_view(template_name='bienvenido.html'), name='bienvenida'),
    path('acerca/', TemplateView.as_view(template_name='acerca_de_nosotros.html'), name='acerca_de_nosotros'),
    path('ayuda/', TemplateView.as_view(template_name='ayuda.html'), name='ayuda'),
    path('politicas/', TemplateView.as_view(template_name='politicas.html'), name='politicas'),
    path('contacto/', TemplateView.as_view(template_name='contacto.html'), name='contacto'),
   path('login/', login_view, name='login'),

    path('nuevo_usuario/', TemplateView.as_view(template_name='nuevo_usuario.html'), name='nuevo_usuario'),
]
