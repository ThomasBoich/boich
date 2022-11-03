from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse_lazy
from rest_framework.response import Response
from rest_framework.views import APIView
from index.models import Rabota, ProjectType


## ГЛАВНАЯ СТРАНИЦА
def index(request):
    context = {
        'title':'Боич - технологии, опережающие время',
        'rabota1': Rabota.objects.get(pk=1),
        # 'rabota2': Rabota.objects.get(pk=2),
        # 'rabota': Rabota.objects.get(pk=3),
       }
    return render(request, 'index/index.html', context=context)

    
## СТРАНИЦА ВСЕ РАБОТЫ
def raboti(request):
    context = {
        'title':'',
        'raboti': Rabota.objects.all(),
        'kategorii': ProjectType.objects.all(),
        'kolichestvo': Rabota.objects.all().count()
    }
    return render(request, 'index/raboti.html', context=context)


## СТРАНИЦА РАБОТЫ
def rabota(request, slug):
    context = {
        ##
        'rabota_info': Rabota.objects.get(slug=slug)

    }
    return render(request, 'index/rabota.html', context=context)


## СТРАНИЦА КАТЕГОРИИ РАБОТ
def kategorii(request, project_type_slug):
    context = {
        'Title': 'Боич',
        'kategoriya': Rabota.objects.filter(project_type__slug=project_type_slug),
        'kategorii': ProjectType.objects.all(),
        'kategoriya_imya': ProjectType.objects.get(slug=project_type_slug),
        'kategoriya_kolichestvo': Rabota.objects.filter(project_type__slug=project_type_slug).count(),
        'raboti': Rabota.objects.filter(project_type__slug=project_type_slug)

    }
    return render(request, 'index/kategoriya.html', context=context)


## СТРАНИЦА КОМПЕТЕНЦИИ
def kompetencii(request):
    context = {
        'tetle':'',
    }
    return render(request, 'index/kompetencii.html', context=context)


## КЛАСС ГЛАВНОЙ СТРАНИЦЫ
class IndexViewAPI(APIView):
    def get(self, request):
        return Response({'title': 'API'})
    def post(self, request):
        return HttpResponse('Это Пост Запрос')


## СТРАНИЦА ПОЛЬЗОВАТЕЛЬЯ
def dashboard(request):
    if request.user.is_authenticated == False:
        return redirect('login')
    else:
        return render(request, 'index/dashboard.html')


## КЛАСС АВТОРИЗАЦИИ
class LoginViewForm(LoginView):
    form_class = AuthenticationForm
    template_name = 'index/login.html'
    success_url = 'dashboard'
    redirect_authenticated_user = True
    redirect_field_name = 'dashboard'
    def get_success_url(self):
        return reverse_lazy('dashboard')


## КЛАСС РАЗЛОГИНИЩАЦИИ
class LogoutViewForm(LogoutView):
    redirect_field_name = 'login'
    def get_success_url(self):
        return reverse_lazy('login')