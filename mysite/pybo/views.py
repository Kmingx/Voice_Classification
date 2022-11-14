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

    kw = request.POST.get('kw','') # 값
    audiourl = request.POST.get('audiourl','') # 값
    audiourl2 = request.POST.get('audiourl2','') # 값
    print("오디오파일확인",audiourl)
    print("오디오파일확인2",audiourl2)
    kwList = kw.split()
    kwlist2 = []
    #audiourl = request.GET.get('audiourl','') # 값

    if kw:
        for i in kwList:
            print(i)
            menu_list = Menu.objects.order_by('id')
            menu_list = menu_list.filter(
                Q(menuName__icontains=i) |
                Q(Price__icontains=i)
                # Q(content__icontains=kw)
            ).distinct()
            print(type(menu_list))
            kwlist2.append(menu_list)
        #print("저장값 : ",kwlist2[0])
        #print("저장값 : ",kwlist2[1])
        for e in range(len(kwList)):
            menu_list = kwlist2[0] | kwlist2[e]
            #menu_list12 =  menu_list1 | menu_list12
            #menu_list = kwlist2[0]|kwlist2[1]
        #print(result_set2)
        context = {'menu_list':menu_list,'kw': kw}

    return render(request, 'pybo/menu_list.html', context)


    