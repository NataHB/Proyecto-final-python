from django.urls import path
from user import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_request, name='Login'),
    path('registro/', views.register, name='Register'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('editarPerfil/', views.editar_perfil, name='editarPerfil'),
    path('editarPassword/', views.CambiaPassword.as_view(), name='editarPassword'),
    path('perfil/', views.Perfil.as_view(), name='perfil'),
]