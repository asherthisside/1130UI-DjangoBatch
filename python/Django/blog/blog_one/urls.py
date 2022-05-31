from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.blog,name="blog"),
    path('blog/<str:pk>',views.fullblog,name="fullblog"),
    path('login',views.login,name="login"),
    path('signup',views.signup,name="signup"),
    path('logout',views.logout,name="logout"),
]
