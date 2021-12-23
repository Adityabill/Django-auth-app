from django.contrib import admin
from django.urls import path, include
from AuthApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about_us', views.about_us, name='about_us'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('signup', views.signup, name='signup'),
    path('feeds', views.feeds, name='feeds'),
]
