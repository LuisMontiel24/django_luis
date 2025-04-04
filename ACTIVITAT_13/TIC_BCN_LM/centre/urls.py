from django.urls import path
from . import views

app_name = 'centre'

urlpatterns = [
    # Listados
    path('students/', views.student_list, name='student_list'),
    path('teachers/', views.teacher_list, name='teacher_list'),

    # CRUD
    path('student/add/', views.persona_create, {'rol': 'student'}, name='student_add'),
    path('teacher/add/', views.persona_create, {'rol': 'teacher'}, name='teacher_add'),
    path('<int:pk>/edit/', views.persona_update, name='persona_edit'),
    path('<int:pk>/delete/', views.persona_delete, name='persona_delete'),
]