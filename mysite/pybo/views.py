from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Question
from .models import Menu



def index(request):

    menu_list = Menu.objects.order_by('id')
    menucontext = {'menu_list': menu_list}

    return render(request, 'pybo/question_list.html', menucontext)

def indexpage(request):

    return render(request, 'pybo/index.html')

def menuList(request):

    menu_list = Menu.objects.order_by('id')
    menucontext = {'menu_list': menu_list}

    return render(request, 'pybo/menu_list.html', menucontext)