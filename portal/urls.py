from django.urls import path
from . import views

app_name = 'portal'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.custom_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-student/', views.add_student, name='add_student'),
    path('student-details/<int:student_id>/', views.student_details, name='student_details'),
    path('submit-documents/<int:student_id>/', views.submit_documents, name='submit_documents'),
    path('toggle-approval/<int:student_id>/', views.toggle_approval, name='toggle_approval'),
    path('generate-report/<int:student_id>/', views.generate_report, name='generate_report'),
    path('logout/', views.custom_logout, name='logout'),
]