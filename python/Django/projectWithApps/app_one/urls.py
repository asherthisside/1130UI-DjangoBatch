from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('add-new-student', views.addStudent, name='addStudent'),
    path('faculty-data', views.facdata, name='faculty'),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('update/<str:pk>', views.update, name='update'),
    path('add-new-faculty', views.addFac, name='addFaculty'),
    path('form-data', views.display, name='datadisplay'),
    path('post/<str:pk>', views.post, name='post'),
]
