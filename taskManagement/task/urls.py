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
    path('teacher/dashboard/<int:pk>/',views.teacherDashboard,name="teacher_dashboard")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)