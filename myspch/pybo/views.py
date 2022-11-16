# Create your views here.
from django.shortcuts import render
from .models import Question
from .models import Menu
from django.db.models import Q

import time

from . import load

def index(request):

    menu_list = Menu.objects.order_by('id')
    menucontext = {'menu_list': menu_list}

    return render(request, 'pybo/question_list.html', menucontext)

def indexpage(request):

    return render(request, 'pybo/index.html')

#filter 추가
def menuList(request):
    time.sleep(0.5) # 파일다운로드 될동안 시간 지연시킴
    inputaudioPath = load.LoadConfig.audioFileLoad()
    #print(inputaudioPath)
    mask1 = load.LoadConfig.model.predict(inputaudioPath)
    print(mask1) # CLI 분류값 확인
    value, peopleType = load.LoadConfig.classification(mask1)

    #print(mask1)
    kw = request.POST.get('kw','') # 값
    audiourl = request.POST.get('audiourl','') # 값
    audiourl2 = request.POST.get('audiourl2','') # 값
    print("오디오파일확인",audiourl)
    print("오디오파일확인2",audiourl2)
    kwList = kw.split()
    kwlist2 = []
    recommendationList = ['메뉴추천','메뉴 추천','메뉴','추천','추천 메뉴','추천메뉴']
    #audiourl = request.GET.get('audiourl','') # 값

    if kw in recommendationList:
        menu_list = Menu.objects.order_by('id')
        menu_list = menu_list.filter(
            Q(Prefer__icontains=value)
        ).distinct()
        context = {'menu_list':menu_list,'peopleType':peopleType}
        return render(request, 'pybo/menu_list2.html',context)     
    else:
        for i in kwList:
            #print(i)
            menu_list = Menu.objects.order_by('id')
            menu_list = menu_list.filter(
                Q(menuName__icontains=i) |
                Q(Price__icontains=i)
                # Q(content__icontains=kw)
            ).distinct()
            #print(type(menu_list))
            kwlist2.append(menu_list)
        #print("저장값 : ",kwlist2[0])
        #print("저장값 : ",kwlist2[1])
        for e in range(len(kwList)):
            try:
                kwlist2[0] = kwlist2[0] | kwlist2[e]
                menu_list = kwlist2[0]
            except IndexError as e:
                print("오류")
        #print(result_set2)
        context = {'menu_list':menu_list,'kw': kw, 'peopleType':peopleType}
        return render(request, 'pybo/menu_list.html', context)

