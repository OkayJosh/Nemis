"""banana URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .routers import router
from login import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='login/base.html'), name='home'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include(router.urls)),
    path('student', TemplateView.as_view(template_name='student/index.html'), name='student'),
    path('teacher', TemplateView.as_view(template_name='teacher/index.html'), name='teacher'),
    path('project', TemplateView.as_view(template_name='project/index.html'), name='project'),
    path('post', TemplateView.as_view(template_name='post/index.html'), name='post'),
    path('asset', TemplateView.as_view(template_name='asset/index.html'), name='asset'),
    path('school', TemplateView.as_view(template_name='school/index.html'), name='school'),
    path('admin/', admin.site.urls),


# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']
]
