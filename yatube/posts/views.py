from django.shortcuts import get_object_or_404, render
from .models import Post, Group


# Create your views here.
def index(request):
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'title': "Это главная страница проекта Yatube",
        'posts': posts
    }
    return render(request, template, context)


def group_list(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
