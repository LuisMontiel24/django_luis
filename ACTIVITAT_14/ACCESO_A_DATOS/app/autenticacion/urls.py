from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_sin_session, name='login'),
    path('login_session/', views.login_con_session, name='login_con_session'),
    path('inicio/', views.inicio, name='inicio'),
    path('logout/', views.logout_view, name='logout'),
]
