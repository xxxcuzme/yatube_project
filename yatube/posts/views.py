from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def index(request):
    template = 'posts/index.html'
    context = {
        'title': "Это главная страница проекта Yatube"
    }
    return render(request, template, context)


def group_list(request, pk):
    template = 'posts/group_list.html'
    context = {
        'title': "Здесь будет информация о группах проекта Yatube"
    }
    return render(request, template, context)