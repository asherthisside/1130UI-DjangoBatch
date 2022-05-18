from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('faculty-data', views.facdata, name='faculty'),
    path('prem-sir-ka-data', views.premsir, name='prem'),
    path('delete', views.delete, name='delete'),
    path('update', views.update, name='update'),
]
