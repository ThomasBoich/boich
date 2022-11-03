from django.urls import path

from index.views import index, IndexViewAPI, raboti, kompetencii, dashboard, LoginViewForm, LogoutViewForm, rabota, \
    kategorii

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('', index, name='index'),
    path('raboti/', raboti, name='raboti'),
    path('category/<slug:project_type_slug>/', kategorii, name='kategorii'),
    path('rabota/<slug:slug>/', rabota, name='rabota'),
    path('kompetencii', kompetencii, name='kompetencii'),
    path('api/v1/', IndexViewAPI.as_view(), name='api'),
    path('login/', LoginViewForm.as_view(), name='login'),
    path('logout/', LogoutViewForm.as_view(), name='logout'),
]