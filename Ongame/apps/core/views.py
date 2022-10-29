from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect

from apps.user.views import verification
from apps.post.models import Notice


# Create your views here.

def index(request):
    user = False
    if verification(request):
        user = True

    template_name = 'index.html'
    posts = Notice.objects.all().order_by('-id')

    return TemplateResponse(request, template_name, locals())

