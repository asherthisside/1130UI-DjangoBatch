from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.blog,name="blog"),
    path('blog/<str:pk>',views.fullblog,name="fullblog"),
]
