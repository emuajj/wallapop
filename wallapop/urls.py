"""wallapop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from wallapop_app.views import anunci_view,SignUpView,edit_profile,get_anunci,ChangePasswordView,look_profile,newad


from django.urls import path




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',anunci_view,name=""),#/home
    path('accounts/',include("django.contrib.auth.urls")),
    path('signup', SignUpView.as_view(), name="signup"),
    path('profile/', edit_profile, name='profile'),
    path('profile/<int:user>/',look_profile, name='profile_view'),
    path('anunci-details/<int:name>/', get_anunci, name='anunci-details'),
    path('password-change/', ChangePasswordView.as_view(), name='password-change'),
    path('newad/',newad ,name='newad')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
