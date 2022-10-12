from django.urls import path

from index.views import index, IndexViewAPI, raboti, kompetencii, dashboard, LoginViewForm, LogoutViewForm

urlpatterns = [
    path('', index, name='index'),
    path('raboti/', raboti, name='raboti'),
    path('kompetencii', kompetencii, name='kompetencii'),
    path('api/v1/', IndexViewAPI.as_view()),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', LoginViewForm.as_view(), name='login'),
    path('logout/', LogoutViewForm.as_view(), name='logout'),
]