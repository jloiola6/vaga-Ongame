from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
import hashlib

from apps.user.forms import *


# Create your views here.
def verification(request):
    try:
       if request.session['login']:
           return True
    except KeyError:
        return False


def logout(request):
    try:
        del request.session['login']
    except KeyError:
        pass
    return HttpResponseRedirect('/')


def login(request):
    if verification(request):
        return HttpResponseRedirect('/')

    user = False    
    template_name = 'user/login.html'

    if request.method == 'POST':
        login = request.POST.get('username')
        password = request.POST.get('password')
        password = hashlib.md5(password.encode())
        password = password.hexdigest()
        if User.objects.filter(login= login, password= password).exists():
            request.session['login'] = login
            return HttpResponseRedirect('/')
        else:
            error = 'Usuário não Cadsatrado'
    return TemplateResponse(request, template_name, locals())


def register(request):
    template_name = 'user/register.html'
    
    user = False    
    if request.GET.get('edit'):
        user = User.objects.get(login= request.session['login'])
        form = Form_Register(instance= user)
    else:
        form = Form_Register()

    if request.method == 'POST':
        form = Form_Register(request.POST, instance= user)
        if form.is_valid():
            user = form.save()

            password = form.cleaned_data['password']
            password = hashlib.md5(password.encode())
            password = password.hexdigest()
            user.password = password
            user.save()

            return HttpResponseRedirect('/user/login')
        else:
            msg = 'Usuário já Cadsatrado'
    return TemplateResponse(request, template_name, locals())