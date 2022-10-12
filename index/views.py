from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from rest_framework.response import Response
from rest_framework.views import APIView


def index(request):
    context = {
        'title':'Боич - технологии, опережающие время',
    }
    return render(request, 'index/index.html', context=context)

def raboti(request):
    context = {
        'title':'',
    }
    return render(request, 'index/raboti.html', context=context)
def kompetencii(request):
    context = {
        'tetle':'',
    }
    return render(request, 'index/kompetencii.html', context=context)

class IndexViewAPI(APIView):
    def get(self, request):
        return Response({'title': 'API'})
    def post(self, request):
        return HttpResponse('Это Пост Запрос')


def dashboard(request):
    if request.user.is_authenticated == False:
        return redirect('login')
    else:
        return render(request, 'index/dashboard.html')

class LoginViewForm(LoginView):
    form_class = AuthenticationForm
    template_name = 'index/login.html'
    success_url = 'dashboard'
    redirect_authenticated_user = True
    redirect_field_name = 'dashboard'
    def get_success_url(self):
        return reverse_lazy('dashboard')


class LogoutViewForm(LogoutView):
    redirect_field_name = 'login'
    def get_success_url(self):
        return reverse_lazy('login')