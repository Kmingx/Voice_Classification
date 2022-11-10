from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Question
from .models import Menu
from django.db.models import Q


def index(request):

    menu_list = Menu.objects.order_by('id')
    menucontext = {'menu_list': menu_list}

    return render(request, 'pybo/question_list.html', menucontext)

def indexpage(request):

    return render(request, 'pybo/index.html')

def menuList(request):

    kw = request.GET.get('kw','') # 값

    menu_list = Menu.objects.order_by('id')


    if kw:
        menu_list = menu_list.filter(
            Q(menuName__icontains=kw) |
            Q(Price__icontains=kw)
            # Q(content__icontains=kw)
        ).distinct()

        context = {'menu_list':menu_list,'kw': kw}

    return render(request, 'pybo/menu_list.html', context)