"""
URL configuration for payment_list project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.views.static import serve
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include('authentication.urls')),
    path('bills/', include('bills.urls')),  
    path('', include('home.urls')),
    path('about/', include('about.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),
    path('account_settings/', include('account_settings.urls')),
       
]

'''
Social Login
'''
try:
    social_login = 'registration/login_social.html'
    urlpatterns.insert(
        0,
        path('accounts/login/', auth_views.LoginView.as_view(template_name=social_login))
    )
    print('Using', social_login, 'as the login template')
except:
    print('Using registration/login.html as the login template')    
    
    
'''
Favicon
'''    
# Serve the favicon - Keep for later
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
urlpatterns += [
    path('favicon.ico', serve, {
        'path': 'favicon.ico',
        'document_root': os.path.join(BASE_DIR, 'home/static'),
    }
    ),
]


