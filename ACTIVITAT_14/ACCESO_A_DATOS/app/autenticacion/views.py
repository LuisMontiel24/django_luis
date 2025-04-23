from django.shortcuts import render, redirect
from .forms import FormularioLogin
from .models import Usuario

# LOGIN SIN SESSION
def login_sin_session(request):
    mensaje = ''
    if request.method == 'POST':
        form = FormularioLogin(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                usuario = Usuario.objects.get(email=email, password=password)
                context = {'usuario': usuario}
                return render(request, 'inicio.html', context)
            except Usuario.DoesNotExist:
                mensaje = 'Credenciales incorrectas'
    else:
        form = FormularioLogin()
    context = {'form': form, 'mensaje': mensaje}
    return render(request, 'login.html', context)

# LOGIN CON SESSION
def login_con_session(request):
    mensaje = ''
    if request.method == 'POST':
        form = FormularioLogin(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                usuario = Usuario.objects.get(email=email, password=password)
                request.session['usuario_id'] = usuario.id
                return redirect('inicio')
            except Usuario.DoesNotExist:
                mensaje = 'Credenciales incorrectas'
    else:
        form = FormularioLogin()
    context = {'form': form, 'mensaje': mensaje}
    return render(request, 'login.html', context)

# INICIO
def inicio(request):
    if 'usuario_id' not in request.session:
        return redirect('login_con_session')
    usuario = Usuario.objects.get(id=request.session['usuario_id'])
    context = {'usuario': usuario}
    return render(request, 'inicio.html', context)

# LOGOUT
def logout_view(request):
    request.session.flush()
    return redirect('login_con_session')
