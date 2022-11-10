from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Question
from .models import Menu



def index(request):
    # question_list = Question.objects.order_by('-id')
    # context = {'question_list': question_list}

    menu_list = Menu.objects.order_by('id')
    menucontext = {'menu_list': menu_list}

    return render(request, 'pybo/question_list.html', menucontext)

def indexpage(request):

    return render(request, 'pybo/index.html')