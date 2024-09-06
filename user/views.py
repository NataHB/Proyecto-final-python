from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from user.forms import UserEditForm, UserRegisterForm
from user.models import Imagen, User
from django.views.generic import ListView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy



# Create your views here.

def register(request):
    msg_register = ""
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request,"mi_app/index.html") 
        else:
            msg_register = "Error en los datos ingresados"
            msg_register += f" | {form.errors}"

    form = UserRegisterForm()     
    return render(request,"users/registro.html" ,  {"form":form, "msg_register": msg_register}) #CAMBIAR RUTA


def login_request(request):
    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "mi_app/index.html") 

        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login}) 


@login_required 
def editar_perfil(request):
    usuario = request.user

    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=usuario)

        if form.is_valid():
            if form.cleaned_data.get('imagen'):
                if Imagen.objects.filter(user=usuario).exists():
                    imagen = Imagen.objects.get(user=usuario)
                    imagen.imagen = form.cleaned_data.get('imagen')
                    imagen.save()
                else:
                    imagen = Imagen(user=usuario, imagen=form.cleaned_data.get('imagen'))
                    imagen.save()

            form.save()
            return render(request, "mi_app/index.html") 

    else:
        form = UserEditForm(instance=usuario)

    return render(request, 'users/editarUsuario.html', {'form': form}) 


class CambiaPassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'users/editarPassword.html'
    success_url = reverse_lazy('index') 

class Perfil(LoginRequiredMixin, ListView):
    model = User
    context_object_name = 'perfil'
    template_name = 'users/perfil.html'