from django.urls import path
from django.conf import settings

from django.conf.urls.static import static

from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.homePage,name="homepage"),
    path('login/',views.login,name="login"),
    path('student/signup/',views.studentSignup,name="student_signup"),
    path('teacher/signup/',views.teacherSignup,name="teacher_signup"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)