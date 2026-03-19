from django.urls import path
from . import views
from .views import login_view, logout_view, register_view


urlpatterns = [

    # LOGIN

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),

    # STUDENT

    path('', views.student_list, name='student_list'),

    path('student/create/', views.student_create, name='student_create'),

    path('student/<int:pk>/update/',
         views.student_update,
         name='student_update'),

    path('student/<int:pk>/delete/',
         views.student_delete,
         name='student_delete'),

    # COURSE

    path('courses/', views.course_list, name='course_list'),

    path('course/create/',
         views.course_create,
         name='course_create'),

    path('course/<int:pk>/update/',
         views.course_update,
         name='course_update'),

    path('course/<int:pk>/delete/',
         views.course_delete,
         name='course_delete'),

]