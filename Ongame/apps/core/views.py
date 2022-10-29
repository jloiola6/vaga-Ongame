from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect

from apps.user.views import verification
from apps.post.models import Notice
from apps.user.models import User


# Create your views here.

def index(request):
    user = False
    if verification(request):
        user = User.objects.get(login= request.session['login'])

    posts = Notice.objects.all().order_by('-id')
    if request.GET.get('myposts'):
        posts = posts.filter(author= user)


    template_name = 'index.html'

    return TemplateResponse(request, template_name, locals())

