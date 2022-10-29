from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect

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

    template_name = 'user/login.html'

    if request.method == 'POST':
        login = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(login= login, password= password).exists():
            request.session['login'] = login
            return HttpResponseRedirect('/')
        else:
            error = 'Usuário não Cadsatrado'
    return TemplateResponse(request, template_name, locals())


def register(request):
    template_name = 'user/register.html'
    user = False

    form = Form_Register()
    if request.method == 'POST':
        form = Form_Register(request.POST)
        if form.is_valid():
            form.passMb5()
            form.save()
            return HttpResponseRedirect('/user/login')
        else:
            msg = 'Usuário já Cadsatrado'
    return TemplateResponse(request, template_name, locals())