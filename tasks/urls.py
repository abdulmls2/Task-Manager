from django.urls import path
from .views import *
from . import views

from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # login, logout , registration
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),
    path('register/', RegisterView.as_view(), name="register"),

    # Task
    path('', TaskList.as_view(), name="task_list"),
    path('task/<int:pk>/', TaskDetail.as_view(), name="task_detail"),
    path('task/create/', TaskCreate.as_view(), name="task_create"),
    path('task/<int:pk>/update/', TaskUpdate.as_view(), name="task_update"),
    path('task/<int:pk>/delete/', TaskDelete.as_view(), name="task_delete"),

    # forgot password
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="tasks/password_reset.html"), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="tasks/password_reset_sent.html"), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="tasks/password_reset_form.html"), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="tasks/password_reset_done.html"), name ='password_reset_complete'),
]
