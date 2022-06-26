from django.urls import path
from django.conf import settings

from django.conf.urls.static import static

from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.homePage,name="homepage"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name='logout'),
    path('student/signup/',views.studentSignup,name="student_signup"),
    path('teacher/signup/',views.teacherSignup,name="teacher_signup"),
    path('student/dashboard/<int:pk>/',views.studentDashboard,name="student_dashboard"),
    path('teacher/dashboard/<int:pk>/',views.teacherDashboard,name="teacher_dashboard"),
    path('teacher/dashboard/<int:pk>/create_task/',views.createTask,name="teacher_dashboard_create"),
    path('teacher/dashboard/<int:pk>/create_task/submit/',views.submitCreateTask,name="teacher_dashboard_submit_task"),
    path('teacher/dashboard/<int:pk>/update_task/<int:task_id>/',views.updateTask,name="teacher_dashboard_create"),
    path('teacher/dashboard/<int:pk>/update_task/<int:task_id>/submit/',views.submitUpdateTask,name="teacher_dashboard_submit_task"),
    path('teacher/dashboard/<int:pk>/view_task/<int:task_id>/',views.viewTask,name="teacher_dashboard"),
    path('teacher/dashboard/<int:pk>/view_task/<int:task_id>/add_student/',views.addStudentToTask,name="teacher_dashboard"),
    path('teacher/dashboard/<int:pk>/delete_task/<int:task_id>/',views.deleteTask,name="teacher_dashboard")

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)