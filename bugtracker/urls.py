"""bugtracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bug/',include('bug.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('product/', include('product.urls')),
    path('', TemplateView.as_view(template_name='home.html'),name='home'),

]
"""
'django.contrib.auth.urls' includes below:
users/login/ [name='login']
users/logout/ [name='logout']
users/password_change/ [name='password_change']
users/password_change/done/ [name='password_change_done']
users/password_reset/ [name='password_reset']
users/password_reset/done/ [name='password_reset_done']
users/reset/<uidb64>/<token>/ [name='password_reset_confirm']
users/reset/done/ [name='password_reset_complete']
"""
