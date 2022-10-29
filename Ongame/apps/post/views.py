from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect

from apps.user.models import User
from apps.core.actions import save_history
from apps.user.views import verification
from apps.post.models import Notice, Comment
from apps.post.uploads import handle_uploaded_file
from apps.post.forms import FormNew


# Create your views here.
def notice(request):
    user = False
    if verification(request):
        user = User.objects.get(login= request.session['login'])

    template_name = 'post/notice.html'
    id = request.GET.get('id')
    post = Notice.objects.get(id= int(id))
    comments = Comment.objects.filter(notice= post)

    if request.method == 'POST':
        comment = Comment()
        comment.author = user
        comment.text = request.POST.get('comment')
        comment.notice = post
        comment.save()

        save_history(False, user, comment.id, 'Comment', comment.create_at)

    return TemplateResponse(request, template_name, locals())


def add(request):
    if not verification(request):
        return HttpResponseRedirect('/user/login')
    
    user = User.objects.get(login= request.session['login'])
    template_name = 'post/add.html'
        
    new = FormNew()
    if request.method == 'POST':
        new = FormNew(request.POST, request.FILES)
        image = False
        if request.FILES.get('image'):
            image = True
            format_file = str(request.FILES.get('image')).split('.')[-1]

        if new.is_valid():
            notice = new.save()
            notice.author = user
            if image:
                title = (notice.title).replace(' ', '-')
                path = f'static/media/{notice.id}-{title}'
                name = 'Imagem.' + format_file
                path_image = handle_uploaded_file(request.FILES['image'], path, name)
                notice.image = path_image
            notice.save()

            save_history(False, user, notice.id, 'Notice', notice.create_at)
            return HttpResponseRedirect('/')
    return TemplateResponse(request, template_name, locals())