from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect

from apps.user.forms import *


# Create your views here.
def verification(request):
    try:
       if request.session['id']:
           return True
    except KeyError:
        return False


def logout(request):
    try:
        del request.session['id']
    except KeyError:
        pass
    return HttpResponseRedirect('/')


def login(request):
    if verification(request):
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        login = request.POST.get('Login')
        password = request.POST.get('Password')
        user = User.objects.get(login= login, password= password)
        if user:
            request.session['id'] = user.id
            return HttpResponseRedirect('/home')
        else:
            msg = 'Usuário não Cadsatrado'
    return TemplateResponse(request, 'login.html', locals())


def register(request):
    form = Form_Register()
    if request.method == 'POST':
        form = Form_Register(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login')
        else:
            msg = 'Usuário já Cadsatrado'
    return TemplateResponse(request, 'register.html', locals())